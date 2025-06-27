# flake8: noqa
# pylint: disable=wildcard-import,unused-wildcard-import,undefined-variable
# turtle imports - ignore IDE warnings
from turtle import *

# 원 개수
n = 10

# 배경색 설정
bgcolor("black")

# 선 색상과 채우기 색상 설정
color("green", "yellow")

# 속도 설정
speed(1)

# 원을 반복해서 그리기
for i in range(n):
    begin_fill()      # 채우기 시작
    circle(80)        # 원 그리기
    end_fill()        # 채우기 끝
    left(360 / n)     # 회전

