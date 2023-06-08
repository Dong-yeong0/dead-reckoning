# dead-reckoning

Kevin, 6/8/2023

### PDR(Pedestrian Dead Reckoning) algorithm

Accelerometer(가속도), Geomagnetic(지자기), Gyroscope(자이로스코프)를 이용하여 사용자의 움직임을 분석하여 이전의 알려진 위치로 부터 현재의 위치를 추정하는 실내 및 실외 위치 인식 기법이다.

### PDR의 예측 변수

1. 걸음 수
2. 보폭
3. 방향

이 3가지 이며, 스마트폰의 accelerometer, geomagnetic, gyroscope sensor를 이용하여 적분 과정을 통한 보행 거리 및 방향 위치를 추정하는 기법.

### 추정 기준

1. 보폭 추정 (Stride length estimation)
2. 방향 추정 (Heading estimation)
3. 걸음 수 추정 (Step counting)

이 3가지를 결합해 사용자의 위치를 추정

### Development environment

* OS: Windows 10
* IDE: VScode

### Set environment

```shell
# install virturalenv
virturalenv venv

# enable venv
.\venv\Scripts\activate

# install numpy, pyproj
(venv) pip install -r .\Document\requirements.txt

# run python script
python dead-reckoning.py
```
