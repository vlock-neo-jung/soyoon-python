# flake8: noqa
# pylint: disable=wildcard-import,unused-wildcard-import,undefined-variable
# turtle imports - ignore IDE warnings
from turtle import *

# 여러 색상의 원 그리기 (회전 포함)

# 원의 수와 색상 정의
num = 5
colors = ['red', 'blue', 'green', 'orange', 'purple']

# 원 그리기
for i in range(num):
    begin_fill()
    color(colors[i])
    circle(100)
    end_fill()
    right(360 / num)  # 등간격 회전
