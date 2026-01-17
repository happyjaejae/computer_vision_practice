from pathlib import Path
from ultralytics import YOLO
import cv2

model_path = Path("runs/detect/train7/weights/best.pt")

# 파일 존재 확인
if not model_path.exists():
    print(f"오류: {model_path} 파일이 존재하지 않습니다")
    # last.pt로 대체
    model_path = Path("runs/detect/train7/weights/last.pt")
    if not model_path.exists():
        print("last.pt도 없습니다. 학습을 먼저 진행하세요.")
        exit()

model = YOLO(model_path)
image_path = "datasets/valid/images/abc.jpg"
results = model(image_path)


for result in results:
    result.show() # 화면에 결과 띄우기
    result.save(filename='result.jpg') # 결과 이미지 저장