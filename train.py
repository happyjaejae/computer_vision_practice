from ultralytics import YOLO

# 1. 모델 로드 (YOLOv8 nano 버전 사용)
model = YOLO("yolov8n.pt") 

# 2. 모델 학습 시작
# data에는 위에서 만든 yaml 파일 경로를 입력합니다.
# epochs는 학습 반복 횟수입니다.
model.train(data="data.yaml", epochs=10, imgsz=640)