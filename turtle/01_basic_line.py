# 01. 기본 선 그리기
# 가장 간단한 turtle 예제입니다

import turtle

# 거북이 객체 생성
t = turtle.Turtle()

# 거북이 속도 설정 (1~10, 숫자가 클수록 빨라짐)
t.speed(1)

# 앞으로 100만큼 이동 (선이 그어짐)
t.forward(100)

# 그래픽 완료 (창이 유지됨)
turtle.done() 