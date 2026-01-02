import cv2
import numpy as np
import os

# 스크립트 파일 위치 기준으로 경로 설정
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'Lenna.jpg')

# 디버깅: 현재 작업 디렉토리 확인
print(f"현재 작업 디렉토리: {os.getcwd()}")
print(f"이미지 경로: {image_path}")

# 파일 존재 확인
if os.path.exists(image_path):
    print("✓ Lenna.png 찾음")
else:
    print("✗ Lenna.png 없음")

# 이미지 로드 (수정된 경로 사용)
image = cv2.imread(image_path)

# 이미지 로드 확인 (추가)
if image is None:
    print("이미지를 읽을 수 없습니다. 파일 경로를 확인하세요.")
    exit()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 빨간색 범위 지정 (HSV)
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# 마스크 생성 및 합치기
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = mask1 + mask2

# 결과 추출 및 저장
result = cv2.bitwise_and(image, image, mask=mask)
result_path = os.path.join(script_dir, 'red_result.jpg')
cv2.imwrite(result_path, result)
print(f"결과 저장 완료: {result_path}")
