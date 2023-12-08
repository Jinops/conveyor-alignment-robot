# Author: Subin Lim

import math

# 5도 이하로 기울어진 것은 정상으로 가정
radian = math.radians(5)

# 실수 값 8개 리스트로 받기
list = [702.6933997824381, 188.96310868445823, 614.2342629477935, 581.3888278593972, 13.126135018173954, 445.86792608139933, 101.60427800001344, 53.47593600000372]

# 함수에 리스트 대입
def get_distance(width, height, input_list):
    print('get_distance', width, height, input_list)
   # y값 중 가장 작은 값을 y1으로 고정하고 시계방향으로 정렬
    y1 = min(input_list[1], input_list[3], input_list[5], input_list[7])
    y1_index = input_list.index(y1)

    box = [y1]
    index = y1_index

    for i in range(7):
        index = (index + 1) % len(input_list)
        box.append(input_list[index])

    box.insert(0, box.pop())

    x1 = box[0]
    y1 = box[1]
    x2 = box[2]
    y2 = box[3]
    x3 = box[4]
    y3 = box[5]
    x4 = box[6]
    y4 = box[7]

    # 움직여야 하는 양 mo (0-100 단위로 안하고 프레임 단위로 나옴)
    mo = 0
    h = y1 # 바닥에서 떨어진 정도
    tan = (y2 - y1) / (x2 - x1)

    # 각도는 정상인지 아닌지 구분하는데만 사용하고 움직이는 정도는 좌푯값으로 결정

    # 박스의 가로 세로 길이 정의
    if (x2 - x1) ** 2 + (y2 - y1) ** 2 > (x4 - x1) ** 2 + (y4 - y1) ** 2:
        xx = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        yy = math.sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
    else:
        xx = math.sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
        yy = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    #  정상인 경우, 세로로 된 경우, 정방향인 경우, 역방향인경우
    if abs(tan) < math.tan(radian) and x2 - x1 > y4 - y1:
        mo = 0
    elif abs(tan) < math.tan(radian) and x2 - x1 < y4 - y1:
        mo = height - y4 + 0.5*(y4 - y1)
    elif (x2 - x1) ** 2 + (y2 - y1) ** 2 > (x4 - x1) ** 2 + (y4 - y1) ** 2:
        mo = height - y3 + (0.5 * (y3 - y4))
    else:
        if y4 > yy:
            mo = height - y3 + 0.5*(y3 - y1)
        else:
            mo = height - y1

    return mo
    