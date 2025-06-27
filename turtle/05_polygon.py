# 05. 다각형 그리기
# 이번에는 원하는 다각형을 그려보겠습니다. 수학적으로 생각해봐야 해요!

import turtle

print("🔷 다각형 그리기 연습")
print("정사각형부터 시작해서 원하는 다각형까지 그려보겠습니다!")

# 거북이 객체 생성
t = turtle.Turtle()

# 1단계: 정사각형 그리기 (4각형)
print("1단계: 정사각형 그리기")

t.speed(1)

# 색상 설정
t.color("blue")  

# 채우기 시작
t.begin_fill()

# 정사각형 그리기
for i in range(4):
    t.forward(100)
    t.left(90)

# 채우기 끝
t.end_fill()


turtle.done() 