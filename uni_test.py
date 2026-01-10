import numpy as np
import pytest
import cv2
import open3d as o3d

# 샘플 함수: 가짜 깊이 맵 생성
def generate_depth_map(image):
    if image is None:
        raise ValueError("입력된 이미지가 없습니다.")
    
    # 흑백 변환 (3채널 -> 1채널)
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 가짜 깊이 맵 적용 (1채널 -> 3채널 컬러맵)
    depth_map = cv2.applyColorMap(grayscale, cv2.COLORMAP_JET)
    return depth_map

# 테스트 코드
def test_generate_depth_map():
    # 테스트용 검정색 빈 이미지 생성 (100x100, 3채널)
    image = np.zeros((100, 100, 3), dtype=np.uint8) 
    
    # 함수 실행
    depth_map = generate_depth_map(image)

    # 검증 1: 출력 크기가 입력 크기와 동일한지 확인
    assert depth_map.shape == image.shape, "출력 크기가 입력 크기와 다릅니다."
    
    # 검증 2: 출력 데이터 타입이 numpy array인지 확인
    assert isinstance(depth_map, np.ndarray), "출력 데이터 타입이 ndarray가 아닙니다."

def test_generate_depth_map_value_range():
    """생성된 Depth Map의 픽셀 값이 유효 범위(0~255) 내에 있는지 검증"""
    image = np.random.randint(0, 256, (50, 50, 3), dtype=np.uint8)
    depth_map = generate_depth_map(image)
    
    # 최소값 0 이상, 최대값 255 이하인지 확인
    assert depth_map.min() >= 0, "픽셀 값이 0보다 작습니다."
    assert depth_map.max() <= 255, "픽셀 값이 255보다 큽니다."

def test_generate_depth_map_various_sizes():
    """다양한 크기(아주 작은 이미지, 직사각형 등)에서도 작동하는지 검증"""
    # 1. 아주 작은 1x1 이미지
    tiny_img = np.zeros((1, 1, 3), dtype=np.uint8)
    depth = generate_depth_map(tiny_img) 
    assert depth.shape == (1, 1, 3)
    
    # 2. 직사각형 이미지 (너비 > 높이)
    rect_img = np.zeros((30, 50, 3), dtype=np.uint8)
    depth = generate_depth_map(rect_img)
    assert depth.shape == (30, 50, 3)

def test_input_validation():
    """잘못된 입력(Numpy 배열이 아닌 경우 등)에 대한 예외 처리 검증"""
    with pytest.raises(Exception): 
        generate_depth_map("This is not an image")

# pytest 실행
if __name__ == "__main__":
    pytest.main(["-v", __file__])