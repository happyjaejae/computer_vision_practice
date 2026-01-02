import cv2
import numpy as np
import os
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
    # 1. 결과 저장 폴더 생성 (없으면 생성)
    output_dir = 'preprocessed_samples'
    os.makedirs(output_dir, exist_ok=True)
    
    # 2. 이미지 5장 처리 및 저장 반복문 (예시: Lenna.jpg를 5번 다르게 저장하거나 다른 이미지 사용)
    for i in range(1, 6):
        # 실제로는 서로 다른 이미지를 불러오거나, 여기서 다양한 증강(회전 등)을 추가 적용
        processed = preprocess_image('Lenna.jpg') 
        
        if processed is not None:
            save_path = f"{output_dir}/sample_{i}.jpg"
            cv2.imwrite(save_path, processed)
            print(f"Saved: {save_path}")
        else:
            print(f"Failed to process sample {i}")