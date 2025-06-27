# 02_square.py - 정사각형 그리기
"""
반복문을 사용해서 정사각형을 그리는 예제입니다.
90도씩 4번 회전하는 과정을 천천히 관찰해보세요!
"""

import turtle

# 화면 설정
screen = turtle.Screen()
screen.title("정사각형 그리기")
screen.bgcolor("lightgray")

# 거북이 설정
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.pensize(3)
t.speed(2)  # 더 느린 속도로 설정

print("정사각형을 그리는 중...")
print("90도씩 4번 회전하는 모습을 관찰해보세요!")

# 정사각형 그리기 (반복문 사용)
for i in range(4):
    print(f"{i+1}번째 변을 그리는 중...")
    t.forward(150)    # 앞으로 150만큼
    t.left(90)        # 왼쪽으로 90도 회전

print("정사각형 완성! 창을 클릭하면 종료됩니다.")
screen.exitonclick() 