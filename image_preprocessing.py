import cv2
import numpy as np
# 필요 시 datasets 라이브러리 설치: pip install datasets
# from datasets import load_dataset 

def preprocess_image(image_path):
    # 1. 이미지 로드 및 크기 조정 (224x224)
    img = cv2.imread(image_path)
    if img is None: return None
    img_resized = cv2.resize(img, (224, 224))

    # 2. [심화] 이상치 탐지 (너무 어두운 이미지 제거)
    avg_brightness = np.mean(cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY))
    if avg_brightness < 30: # 기준값 예시
        print("Filtered: Image too dark")
        return None

    # 3. 색상 변환 (Grayscale) 및 노이즈 제거 (Blur)
    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 4. 데이터 증강 (좌우 반전 등)
    augmented = cv2.flip(blurred, 1) 
    
    return augmented

# 실행 및 결과 저장 로직을 추가하여 작성하세요.
if __name__ == "__main__":
    processed = preprocess_image('Lenna.jpg')
    if processed is not None:
        cv2.imwrite('preprocessed_Lenna.jpg', processed)
        print("Preprocessing completed and saved.")
    else:
        print("Preprocessing failed.")