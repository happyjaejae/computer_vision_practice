import cv2
import numpy as np
import os

# 디버깅: 현재 작업 디렉토리 확인
print(f"현재 작업 디렉토리: {os.getcwd()}")
print(f"현재 폴더의 파일들:")
for file in os.listdir('.'):
    print(f"  - {file}")

# 파일 존재 확인
if os.path.exists('Lenna.png'):
    print("✓ Lenna.png 찾음")
else:
    print("✗ Lenna.png 없음")

image = cv2.imread('Lenna.png')

# 이미지 로드 (경로는 실제 파일명에 맞게 수정)
image = cv2.imread('Lenna.jpg') 
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
cv2.imwrite('red_result.jpg', result) # 결과 확인용 저장