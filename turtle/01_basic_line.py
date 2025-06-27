# 01_basic_line.py - 기본 선 그리기
"""
turtle의 가장 기본적인 기능인 선 그리기 예제입니다.
거북이가 천천히 움직이는 모습을 관찰해보세요!
"""

import turtle

# 화면 설정
screen = turtle.Screen()
screen.title("기본 선 그리기")
screen.bgcolor("white")

# 거북이 설정
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(3)  # 느린 속도로 설정 (1~10, 숫자가 작을수록 느림)

print("거북이가 선을 그리는 모습을 관찰해보세요!")

# 간단한 선 그리기
t.forward(100)
t.left(90)
t.forward(100)
t.right(45)
t.forward(100)

# 클릭하면 창 종료
print("그리기 완료! 창을 클릭하면 종료됩니다.")
screen.exitonclick() 