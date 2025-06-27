# 04. 삼각형 그리기
# 반복문을 사용해서 효율적으로 삼각형을 그려봅시다

import turtle

print("🔺 삼각형 그리기 연습")
print("반복문으로 삼각형을 그리고, 색상으로 채워보겠습니다!")

# 거북이 객체 생성
t = turtle.Turtle()

# 첫 번째: 간단한 삼각형 그리기
print("1단계: 간단한 삼각형 그리기")

t.speed(3)

# for문으로 3번 반복
for i in range(3):
    t.forward(100)    # 앞으로 100만큼
    t.left(120)       # 왼쪽으로 120도 회전 (삼각형의 외각)

print("✅ 첫 번째 삼각형 완성!")

turtle.done() 