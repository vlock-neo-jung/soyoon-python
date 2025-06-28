"""
tkinter의 Canvas를 사용한 도형 그리기 예제
- Canvas: 선, 원, 사각형, 다각형 등을 그릴 수 있는 화면
- 다양한 모양과 색상으로 그림을 그릴 수 있습니다
"""

# tkinter 라이브러리 불러오기 (GUI 윈도우를 만들기 위해 필요)
import tkinter as tk

# 윈도우(창) 객체 생성
# tk.Tk(): 새로운 윈도우를 만드는 함수
root = tk.Tk()

# Canvas 객체 생성
# Canvas: 그림을 그릴 수 있는 도화지 같은 공간
# width: 캔버스의 가로 크기
# height: 캔버스의 세로 크기
# bg: 캔버스의 배경색
canvas = tk.Canvas(
    root,                      # 어느 윈도우에 캔버스를 넣을지
    width=400,                 # 캔버스 가로 크기 (픽셀)
    height=300,                # 캔버스 세로 크기 (픽셀)
    bg="white"                 # 캔버스 배경색 (흰색)
)

# 캔버스를 윈도우에 배치
# pack(): 위젯을 윈도우에 배치하는 함수
canvas.pack()

# 선 그리기
# create_line(x1, y1, x2, y2): 시작점(x1,y1)에서 끝점(x2,y2)까지 선을 그림
# fill: 선의 색상
# width: 선의 두께
canvas.create_line(
    50, 50,                    # 시작점 좌표 (x=50, y=50)
    350, 50,                   # 끝점 좌표 (x=350, y=50)
    fill="black",              # 선 색상 (검은색)
    width=3                    # 선 두께 (3픽셀)
)

# 사각형 그리기
# create_rectangle(x1, y1, x2, y2): 왼쪽위(x1,y1)에서 오른쪽아래(x2,y2)까지 사각형
# fill: 사각형 내부 색상
canvas.create_rectangle(
    50, 100,                   # 왼쪽 위 모서리 좌표
    200, 200,                  # 오른쪽 아래 모서리 좌표
    fill="blue"                # 사각형 색상 (파란색)
)

# 원 그리기
# create_oval(x1, y1, x2, y2): 사각형 안에 맞는 타원(원) 그리기
# fill: 원 내부 색상
canvas.create_oval(
    220, 100,                  # 원을 감싸는 사각형의 왼쪽 위
    350, 200,                  # 원을 감싸는 사각형의 오른쪽 아래
    fill="red"                 # 원 색상 (빨간색)
)

# 삼각형(다각형) 그리기
# create_polygon(): 여러 점을 연결해서 다각형 그리기
# 점들의 좌표를 순서대로 나열
canvas.create_polygon(
    150, 250,                  # 첫 번째 점 (삼각형의 맨 위)
    250, 250,                  # 두 번째 점 (삼각형의 오른쪽 아래)
    200, 180,                  # 세 번째 점 (삼각형의 왼쪽 아래)
    fill="green"               # 삼각형 색상 (초록색)
)

# 텍스트 추가
# create_text(x, y): 지정한 위치에 글자 쓰기
# text: 표시할 글자
# font: 글자체, 크기 설정
canvas.create_text(
    200, 30,                   # 텍스트가 표시될 위치
    text="Canvas 요소 예제!",   # 표시할 글자
    font=("Arial", 16)         # 글자체와 크기
)

# 윈도우를 화면에 표시하고 프로그램 실행
# mainloop(): 윈도우를 계속 띄워두고 사용자의 행동을 기다리는 함수
root.mainloop()

# 🎯 연습과제들 (아래 숫자를 바꿔보세요!)
#
# 📝 연습과제 1: 도형 위치 바꿔보기
# - 선: canvas.create_line(100, 80, 300, 80, fill="black", width=3)
# - 사각형: canvas.create_rectangle(80, 120, 180, 180, fill="blue")
# - 원: canvas.create_oval(250, 120, 320, 180, fill="red")
#
# 📝 연습과제 2: 도형 크기 바꿔보기
# - 더 큰 사각형: canvas.create_rectangle(30, 80, 250, 220, fill="blue")
# - 더 작은 원: canvas.create_oval(240, 120, 300, 160, fill="red")
# - 더 긴 선: canvas.create_line(20, 50, 380, 50, fill="black", width=3)
#
# 📝 연습과제 3: 도형 색상 바꿔보기
# - fill="purple"    # 보라색
# - fill="orange"    # 주황색  
# - fill="pink"      # 분홍색
# - fill="yellow"    # 노란색
#
# 📝 연습과제 4: 선 두께나 텍스트 바꿔보기
# - width=5          # 더 두꺼운 선
# - width=1          # 더 얇은 선
# - text="내가 그린 그림!"  # 다른 텍스트
# - font=("Arial", 20)     # 더 큰 글자


