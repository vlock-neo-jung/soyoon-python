# 04_polygon.py - 다각형 그리기
"""
사용자가 원하는 다각형을 그리는 예제입니다.
수학적 계산 (360 ÷ n)을 통해 다양한 도형을 만들어보세요!
"""

import turtle

# 화면 설정
screen = turtle.Screen()
screen.title("다각형 그리기")
screen.bgcolor("lightblue")

# 거북이 설정
t = turtle.Turtle()
t.shape("turtle")
t.color("purple")
t.pensize(3)
t.speed(4)  # 적당한 속도

# 사용자로부터 다각형의 변의 수 입력받기
n = int(screen.textinput("다각형 그리기", "몇 각형을 그릴까요? (3 이상의 숫자)"))

if n < 3:
    print("3 이상의 숫자를 입력해주세요!")
    screen.bye()
else:
    angle = 360 / n  # 회전 각도 계산
    
    print(f"{n}각형을 그리는 중...")
    print(f"각 꼭짓점에서 {angle:.1f}도씩 회전합니다.")
    
    # n각형 그리기
    for i in range(n):
        print(f"{i+1}번째 변을 그리는 중...")
        t.forward(100)
        t.left(angle)
    
    print(f"{n}각형 완성!")
    print("창을 클릭하면 종료됩니다.")
    screen.exitonclick() 