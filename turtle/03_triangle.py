# 03_triangle.py - 삼각형 그리기
"""
색상이 채워진 삼각형을 그리는 예제입니다.
120도씩 3번 회전하는 과정과 색상 채우기를 관찰해보세요!
"""

import turtle

# 화면 설정
screen = turtle.Screen()
screen.title("삼각형 그리기")
screen.bgcolor("pink")

# 거북이 설정
t = turtle.Turtle()
t.shape("turtle")
t.color("blue", "yellow")  # 선은 파란색, 채우기는 노란색
t.pensize(4)
t.speed(3)  # 적당한 속도

print("색상이 채워진 삼각형을 그리는 중...")
print("120도씩 3번 회전하는 모습을 관찰해보세요!")

# 채우기 시작
t.begin_fill()

# 삼각형 그리기
for i in range(3):
    print(f"{i+1}번째 변을 그리는 중...")
    t.forward(200)    # 앞으로 200만큼
    t.left(120)       # 왼쪽으로 120도 회전 (삼각형의 외각)

# 채우기 끝
t.end_fill()

print("삼각형 완성! 노란색으로 채워졌습니다.")
print("창을 클릭하면 종료됩니다.")
screen.exitonclick() 