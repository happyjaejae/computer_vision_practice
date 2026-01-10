# Computer Vision & Git Practice Project

## 📝 프로젝트 개요
이 프로젝트는 **Computer Vision**의 핵심 기초를 다지고, 현업 수준의 **Git 워크플로우**를 체화하기 위해 수행되었습니다.
단순한 2D 이미지 처리를 넘어, **3D Point Cloud 변환** 기술을 실습하고 **Unit Test(단위 테스트)**를 통해 코드의 안정성을 검증하는 전체 파이프라인을 구축했습니다.

## 📂 폴더 구조
computer_vision_practice
├── main.py # 2D to 3D 변환 및 시각화 메인 코드 (2주차)
├── image_preprocessing.py # 이미지 전처리 및 증강 코드 (1주차)
├── red_filter.py # 특정 색상(Red) 검출 코드 (1주차)
├── uni_test.py # 단위 테스트(Unit Test) 코드 (2주차)
├── requirements.txt # 의존성 패키지 목록
└── README.md # 프로젝트 문서

## 🛠️ 기술 스택 (Tech Stack)
- **Language**: Python 3.11.5
- **Libraries**:
  - **OpenCV**: 이미지 처리 및 Depth Map 생성
  - **NumPy**: 고속 행렬 연산 및 3D 좌표계 계산
  - **Open3D**: 3D Point Cloud 시각화 및 파일 저장
  - **Pytest**: 코드 기능 검증 및 테스트 자동화

## 🚀 주요 기능
### 1. 1차 업무: 픽셀 단위 이미지 처리 (Image Processing)
OpenCV를 활용하여 이미지 데이터를 분석하고 전처리하는 기초 로직을 구현했습니다.
- **특정 색상 검출**: HSV 색상 공간을 활용한 빨간색 영역 마스킹 (`red_filter.py`)
- **데이터 전처리/증강**: 이미지 크기 조정 (Resize), 노이즈 제거 (Blur), 이상치 탐지 및 데이터 증강(Flip) (`image_preprocessing.py`)

### 2. 2차 업무: 2D → 3D 변환 및 테스트 (3D Vision & Unit Test)
2D 이미지를 3차원 데이터로 변환하고, 이를 시각화 및 검증했습니다.
- **Depth Map 생성**: 입력 이미지의 밝기 정보를 기반으로 가상 깊이(Pseudo-depth) 맵 생성
- **Point Cloud 변환**: 2D 픽셀 좌표(X, Y)와 깊이 정보(Z)를 결합하여 3D 점군 데이터(Point Cloud) 생성 및 `.ply` 저장
- **3D 시각화**: Open3D를 활용한 대화형 3D 뷰어 및 법선벡터(Normals) 렌더링
- **Unit Test**: `pytest`를 활용하여 입출력 크기 검증, 예외 처리, 값의 유효성 등 코드 무결성 검증 (`uni_test.py`)

## 💻 설치 및 실행 방법

### 1. 환경 설정
필요한 라이브러리를 설치합니다.
```bash
pip install opencv-python numpy open3d pytest

### 2. 실행 방법
이미지 전처리 (1주차)
```bash
python image_preprocessing.py

3D 변환 및 시각화 (2주차)
```bash
python main.py
실행 시 'Original Image', 'Depth Map' 창과 함께 3D 뷰어가 실행됩니다.

단위 테스트(Unit Test) 수행
```bash
pytest uni_test.py

### 3. 트러블슈팅
- FileNotFoundError 발생 시: 실행 위치에 sample.jpg 혹은 Lenna.jpg 파일이 존재하는지 확인해주세요.
- Open3D 창이 안 뜰 때: 그래픽 드라이버 업데이트 혹은 pip install --upgrade open3d를 시도해보세요.