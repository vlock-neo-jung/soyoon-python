# flake8: noqa
# pylint: disable=wildcard-import,unused-wildcard-import,undefined-variable
# turtle imports - ignore IDE warnings
from turtle import *

n = 50

bgcolor("black")

color("green")

speed(1)

for i in range(n):
    circle(80)
    left(360 / n)
