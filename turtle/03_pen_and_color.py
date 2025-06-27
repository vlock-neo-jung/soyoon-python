# 03. 펜 설정과 색상 꾸미기
# 거북이의 모양, 색상, 선 굵기를 설정해봅시다

import turtle

print("🎨 펜 설정과 색상 꾸미기")
print("다양한 색상으로 꾸며진 선을 확인해주세요!")

# 거북이 객체 생성
t = turtle.Turtle()

# 거북이 모양과 색상 설정
t.shape("turtle")      # 거북이 모양으로 변경
t.color("blue")        # 파란색으로 설정
t.pensize(3)           # 선 굵기를 3으로 설정
t.speed(1)             # 속도 설정 (1~10, 0은 가장 빠름)

print("파란색 선 그리기...")
# 색상이 적용된 선 그리기
t.forward(100)
t.left(90)

print("빨간색으로 변경...")
t.color("red")         # 빨간색으로 변경
t.forward(100)
t.left(90)

print("초록색으로 변경...")
t.color("green")       # 초록색으로 변경
t.forward(100)
t.left(90)

print("보라색으로 변경...")
t.color("purple")      # 보라색으로 변경
t.forward(100)

print("✅ 색상 변경 완료!")
print("이제 더 굵은 선으로 그려봅시다!")

# 선 굵기 더 크게 설정
t.pensize(8)
t.color("orange")

# 큰 삼각형 그리기
for i in range(3):
    t.forward(120)
    t.left(120)

print("🌟 굵고 주황색인 삼각형 완성!")

turtle.done() 