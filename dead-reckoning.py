import numpy as np
from pyproj import Proj, transform

# Constants (상수)
alpha = 0.8     # Weight for accelerometer-based step length estimation (가속도계를 사용한 걸음 길이 추정에 대한 가중치)
beta = 0.2      # Weight for gyroscope-based heading estimation (자이로스코프를 사용한 이동 방향 추정에 대한 가중치)
c = 0.0         # Bias term (편향)


def pdr_algorithm(
    accelerometer_data, gyroscope_data, time_step, initial_lat, initial_lon
):
    """
    accelerometer_data          : 가속도계 데이터를 담은 리스트
    gyroscope_data              : 자이로스코프 데이터를 담은 리스트
    time_step                   : 측정 간격(시간 단위)
    initial_lat, initial_lon    : 초기 위치의 위도와 경도
    """
    # Initialize variables
    step_lengths = []  # 추정된 걸음 길이를 저장하는 리스트
    headings = []  # 추정된 이동 방향을 저장하는 리스트
    positions = [
        (initial_lat, initial_lon)
    ]  # Starting position (latitude, longitude) -> 추정된 위치를 저장하는 리스트

    for i in range(len(accelerometer_data)):
        step_detected = detect_step(accelerometer_data[i])

        if step_detected:
            # Step length estimation (걸음 길이 추정)
            step_length = estimate_step_length(accelerometer_data[i])
            step_lengths.append(step_length)

            # Heading estimation
            heading = estimate_heading(gyroscope_data[i])
            headings.append(heading)

        # Dead reckoning calculation
        if i > 0:
            # Calculate position based on step lengths and headings
            delta_x = (step_lengths[i - 1] + c) * np.sin(np.radians(headings[i - 1]))
            delta_y = (step_lengths[i - 1] + c) * np.cos(np.radians(headings[i - 1]))

            # Convert position to latitude and longitude
            prev_lat, prev_lon = positions[i - 1]
            new_lat, new_lon = add_distances_to_lat_lon(
                prev_lat, prev_lon, delta_x, delta_y
            )

            positions.append((new_lat, new_lon))

    return positions


def detect_step(accelerometer_reading):
    """
    Perform step detection based on accelerometer data
    가속도계 데이터를 기반으로 걸음이 감지되었는지 판단하는 함수
    """
    return True  # return always True, because this function not to been implemented


def estimate_step_length(accelerometer_reading):
    """
    Perform step length estimation based on accelerometer data
    가속도계 데이터를 기반으로 걸음의 길이를 추정하는 함수
    """

    x = accelerometer_reading[0]
    y = accelerometer_reading[1]
    z = accelerometer_reading[2]

    # Perform step length estimation calculation
    # Euclidean 거리를 계산하고 alpha와 c를 고려하여 추정된 걸음 길이를 반환
    step_length = alpha * np.sqrt(x**2 + y**2 + z**2) + c
    print(f"Step length: {step_length}")
    return step_length


def estimate_heading(gyroscope_reading):
    """
    Perform heading estimation based on gyroscope data
    자이로스코프 데이터를 기반으로 이동 방향(heading)을 추정하는 함수
    """
    # Implement your own heading estimation algorithm or use existing techniques
    x = gyroscope_reading[0]
    y = gyroscope_reading[1]
    z = gyroscope_reading[2]

    # Perform heading estimation calculation
    # beta를 고려하여 각도를 계산하여 이동 방향을 반환
    heading = beta * np.arctan2(y, x)
    print(f"Heading: {heading}")
    return heading


def add_distances_to_lat_lon(lat, lon, dx, dy):
    """
    Convert latitude and longitude to meters
    주어진 위도와 경도에 거리(dx, dy)를 더하여 새로운 위치의 위도와 경도를 계산하는 함수
    """
    p = Proj(proj="utm", zone=33, ellps="WGS84")
    x, y = p(lon, lat)

    x += dx
    y += dy

    # Convert back to latitude and longitude
    # UTM 좌표계를 사용하여 좌표를 변환하고, 변환된 좌표에 거리를 더한 후 다시 위도와 경도로 변환하여 반환
    new_lon, new_lat = p(x, y, inverse=True)

    return new_lat, new_lon


"""
Data
accelerometer_data              : 가속도계 데이터
gyroscope_data                  : 자이로스코프 데이터
time_step                       : 데이터 측정 간격
initial_lat, initial_lon        : 초기 위치의 위도와 경도
"""
accelerometer_data = [
    [1.0, 2.0, 3.0],
    [2.0, 1.5, 3.5],
    [1.5, 1.2, 3.8],
]
gyroscope_data = [
    [0.0, 0.5, -0.2],
    [0.2, -0.1, 0.3],
    [0.3, 0.4, -0.5],
]
time_step = 0.1             # Time step between readings
initial_lat = 0.0           # Initial latitude
initial_lon = 0.0           # Initial longitude

# positions: PDR 알고리즘을 통해 추정된 위치들이 저장되어 있습니다.
positions = pdr_algorithm(
    accelerometer_data, gyroscope_data, time_step, initial_lat, initial_lon
)

for position in positions:
    print(position[0], position[1])
    # print("Latitude:", position[0])
    # print("Longitude:", position[1])
    print()
