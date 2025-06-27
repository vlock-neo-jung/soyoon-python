# flake8: noqa
# pylint: disable=wildcard-import,unused-wildcard-import,undefined-variable
# turtle imports - ignore IDE warnings
from turtle import *

#  3개의 원 그리기 (직접 반복 없이 그리기)

color('blue', 'pink')  # 선 색, 채우기 색 설정
begin_fill()

penup()
goto(-300, 0)
pendown()
circle(100)

penup()
goto(0, 0)
pendown()
circle(100)

penup()
goto(300, 0)
pendown()
circle(100)

end_fill()
