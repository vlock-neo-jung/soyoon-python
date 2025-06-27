# flake8: noqa
# pylint: disable=wildcard-import,unused-wildcard-import,undefined-variable
# turtle imports - ignore IDE warnings
from turtle import *

print("🟢 원 그리기 - import * 방식")

# 배경 설정
bgcolor("lightblue")

# 거북이 설정
speed(3)
color("red")
shape("turtle")

# 원 그리기
circle(50)

print("✅ 빨간색 원 완성!")

# 위치 이동해서 다른 원 그리기
penup()
goto(120, 0)
pendown()

color("blue")
circle(30)

print("✅ 파란색 원도 완성!")

done()