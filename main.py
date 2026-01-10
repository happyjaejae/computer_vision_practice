import cv2
import numpy as np
import open3d as o3d

def main():
    # 1. 이미지 로드
    image_path = 'Lenna.jpg'
    image = cv2.imread(image_path)

    if image is None:
        print(f"오류: '{image_path}' 파일을 찾을 수 없습니다.")
        return

    # 2. 그레이스케일 변환 (깊이 정보 추출을 위한 전처리)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 3. 가짜 깊이 맵(Depth Map) 생성
    # COLORMAP_JET을 적용하여 깊이감을 색상으로 시각화합니다.
    depth_map = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

    # 4. 3D 포인트 클라우드 생성
    # 이미지의 높이(h)와 너비(w) 추출
    h, w = depth_map.shape[:2]

    # 메쉬 그리드 생성: 이미지 크기만큼의 X, Y 좌표 행렬을 만듭니다.
    # X: 열 좌표 (0 ~ w-1), Y: 행 좌표 (0 ~ h-1)
    X, Y = np.meshgrid(np.arange(w), np.arange(h))

    # Z 좌표: 흑백 이미지(gray)의 픽셀 값을 깊이 정보(Z축)로 사용
    Z = gray.astype(np.float32)

    # 3D 좌표 생성: (Height, Width, 3) 형태의 3차원 배열로 병합
    points_3d = np.dstack((X, Y, Z))

    # [Open3D 시각화 코드]
    # 1. 데이터를 Open3D 형식(N행 3열)으로 변환 (평탄화)
    points = points_3d.reshape(-1, 3)

    # 2. 색상 정보 가져오기 (OpenCV는 BGR, Open3D는 RGB 사용)
    colors = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).reshape(-1, 3) / 255.0

    # 3. PointCloud 객체 생성 및 데이터 할당
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd.colors = o3d.utility.Vector3dVector(colors)

    # 포인트 클라우드 저장 (.ply 파일)
    output_filename = "output_pointcloud.ply"
    o3d.io.write_point_cloud(output_filename, pcd)
    print(f"포인트 클라우드가 '{output_filename}'로 저장되었습니다.")

    # 법선 벡터 추정 (시각화 품질 향상)
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

    # 4. 시각화 실행 (이 창을 닫아야 다음 opencv 창이 뜹니다)
    print("3D 뷰어 실행 중... (마우스로 회전/확대 가능)")
    o3d.visualization.draw_geometries([pcd], window_name='3D Point Cloud')

    print(f"3D 포인트 클라우드 생성 완료. 데이터 형태: {points_3d.shape}")
    
    # 5. 결과 시각화
    cv2.imshow('Original Image', image)
    cv2.imshow('Depth Map', depth_map)
    
    # 아무 키나 누르면 창 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()