# flake8: noqa
# pylint: disable=wildcard-import,unused-wildcard-import,undefined-variable
# 05. 다각형 그리기
# 이번에는 원하는 다각형을 그려보겠습니다. 수학적으로 생각해봐야 해요!

from turtle import *

print("🔷 다각형 그리기 연습")
print("정사각형부터 시작해서 원하는 다각형까지 그려보겠습니다!")

# 1단계: 정사각형 그리기 (4각형)
print("1단계: 정사각형 그리기")

speed(1)

# 색상 설정
color("blue")

# 채우기 시작
begin_fill()

# 정사각형 그리기
for i in range(4):
    forward(100)
    left(90)

# 채우기 끝
end_fill()


