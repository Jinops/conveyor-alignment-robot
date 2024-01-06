# conveyor-alignment-robot

detect object's rotation and align robot on conveyor belt

컨베이어벨트 위의 물체 회전량 인식 및 정렬 로봇


https://github.com/Jinops/conveyor-alignment-robot/assets/46846964/0341c5d7-529b-471e-9ff4-080d53e8761a

## 주요 구현
1. 로봇 코드
2. 회전각 계산 알고리즘
3. yolo_obb 모델 및 서버

## 개발 환경
### 로봇
- Mycobot 280 for Arduino (2020)
- Arduino Mega (최소 2쌍의 Rx/Tx 포트 요구)

### 메인PC
- MacOS 12.4
- Python 3.10
- Arduino IDE 2.2.1

### 서버
- Windows 10
- Python 3.10
- cuda toolkit 11.8 (최소 11.3 요구)
- cuda driver 12.2
- RTX3060 그래픽카드

## 흐름

![flow diagram](./flow_diagram.png)

1. 카메라로부터 이미지 촬영
2. 전처리 후 `./predict`로 GPU서버에 이미지 POST
3. GPU서버에서 yolo_obb 모델 돌린 후, 결과(bounding box, confidence, class, ...) 반환
4. 서버 응답으로부터 최선의 bounding box 선정, 이동거리 계산
5. 계산된 결과를 시리얼통신을 통해 아두이노로 전송
6. 아두이노를 통해 calibration을 선행한 뒤, 전달받은 거리만큼 로봇 팔 이동
