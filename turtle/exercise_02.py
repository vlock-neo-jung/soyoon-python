# flake8: noqa
# pylint: disable=wildcard-import,unused-wildcard-import,undefined-variable
# turtle imports - ignore IDE warnings
from turtle import *

# 3개의 원 그리기 (반복문으로 간단히)

color('blue', 'pink')  # 선 색, 채우기 색 설정
begin_fill()

for x in [-300, 0, 300]:
    penup()
    goto(x, 0)
    pendown()
    circle(100)

end_fill()
