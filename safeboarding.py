import cv2
import numpy as np
from ultralytics import YOLO

def analyze_congestion(image_path, output_name):
    # 1. 모델 로드
    model = YOLO('yolov8x.pt') 
    image = cv2.imread(image_path)
    if image is None: return

    h, w = image.shape[:2]
    
    # ROI 설정 (30% ~ 70%)
    roi_x1 = int(w * 0.30) 
    roi_x2 = int(w * 0.70) 
    
    # 2. [성능 업그레이드] TTA(augment=True) 적용
    # 이미지를 여러 각도에서 분석하여 숨겨진 사람까지 찾아냅니다.
    # conf를 0.2로 낮춰서 흐릿한 사람도 잡고, iou를 0.6으로 높여 겹친 사람 허용
    results = model(image, classes=[0], conf=0.2, iou=0.6, augment=True)
    
    standing_count = 0
    
    # 시각화를 위한 오버레이 레이어 생성
    overlay = image.copy()
    
    # 탐지 루프
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            
            # 조건: ROI 안에 있고, 화면 너무 아래(무릎)가 아닐 것
            if roi_x1 < cx < roi_x2 and y1 < h * 0.85:
                standing_count += 1
                # 사람 박스 (진한 빨강)
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
            else:
                # 제외된 사람 (연한 회색, 점선 느낌)
                cv2.rectangle(image, (x1, y1), (x2, y2), (150, 150, 150), 1)

    # 3. 혼잡도 판단 및 고급 시각화
    THRESHOLD = 5
    
    if standing_count >= THRESHOLD:
        status_text = f"DANGER: {standing_count} (STOP)"
        status_color = (0, 0, 255) # Red
        # ROI 영역을 붉은색 반투명으로 칠함
        cv2.rectangle(overlay, (roi_x1, 0), (roi_x2, h), status_color, -1)
    else:
        status_text = f"SAFE: {standing_count} (GO)"
        status_color = (0, 255, 0) # Green
        # ROI 영역을 초록색 반투명으로 칠함
        cv2.rectangle(overlay, (roi_x1, 0), (roi_x2, h), status_color, -1)

    # 4. 반투명 합성 (Alpha Blending)
    alpha = 0.2 # 투명도 (0.0 ~ 1.0)
    image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

    # 5. 텍스트 디자인 (가독성 최적화)
    font_scale = w / 1000.0 * 2.5
    thickness = int(font_scale * 2)
    (text_w, text_h), _ = cv2.getTextSize(status_text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
    
    # 상단 검정 바 (헤더)
    cv2.rectangle(image, (0, 0), (w, int(text_h * 2.5)), (0, 0, 0), -1)
    
    # 텍스트 출력
    text_x = (w - text_w) // 2
    text_y = int(text_h * 1.8)
    cv2.putText(image, status_text, (text_x, text_y), 
                cv2.FONT_HERSHEY_SIMPLEX, font_scale, status_color, thickness)

    # ROI 경계선 그리기 (선명하게)
    cv2.line(image, (roi_x1, 0), (roi_x1, h), status_color, 3)
    cv2.line(image, (roi_x2, 0), (roi_x2, h), status_color, 3)

    cv2.imwrite(output_name, image)
    print(f"[{output_name}] 정밀 분석 완료: {standing_count}명 감지됨.")

if __name__ == "__main__":
    analyze_congestion("crowded.jpg", "result_crowded.jpg")
    analyze_congestion("empty.jpg", "result_empty.jpg")