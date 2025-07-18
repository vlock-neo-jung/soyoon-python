"""
tkinter를 사용한 공 튀기기 애니메이션 예제
- Canvas에서 공을 움직이고 벽에 부딪히면 방향을 바꾸는 프로그램
- 시간 기반 애니메이션의 기본 원리를 학습할 수 있습니다
"""

# tkinter 라이브러리 불러오기 (GUI 윈도우를 만들기 위해 필요)
import tkinter as tk

# 윈도우(창) 객체 생성
# tk.Tk(): 새로운 윈도우를 만드는 함수
root = tk.Tk()

# 윈도우 제목 설정
root.title("공 튀기기 애니메이션")

# Canvas 객체 생성 (공이 움직일 공간)
# Canvas: 그림을 그리고 애니메이션을 만들 수 있는 도화지
canvas = tk.Canvas(
    root,                      # 어느 윈도우에 캔버스를 넣을지
    width=400,                 # 캔버스 가로 크기
    height=300,                # 캔버스 세로 크기
    bg="white"                 # 캔버스 배경색 (흰색)
)

# 캔버스를 윈도우에 배치
canvas.pack()

# 공 생성
# create_oval(): 원(공) 그리기
# 좌표는 공을 감싸는 사각형의 왼쪽위, 오른쪽아래 모서리
ball = canvas.create_oval(
    50, 50,                    # 공의 왼쪽 위 모서리
    80, 80,                    # 공의 오른쪽 아래 모서리 (30x30 크기의 공)
    fill="red"                 # 공의 색상 (빨간색)
)

# 공의 이동 거리 (속도) 설정
# dx: x방향(가로) 이동 거리 (양수면 오른쪽, 음수면 왼쪽)
# dy: y방향(세로) 이동 거리 (양수면 아래, 음수면 위)
dx, dy = 5, 3                  # 5픽셀씩 오른쪽, 3픽셀씩 아래로


# 공을 움직이는 함수 정의
def move_ball():
    """공을 움직이고 벽에 부딪히면 방향을 바꾸는 함수"""
    # global: 함수 밖의 변수를 함수 안에서 수정하기 위해 사용
    global dx, dy
    
    # 현재 공의 위치 좌표 가져오기
    # coords(): 객체의 현재 좌표를 반환하는 함수
    x1, y1, x2, y2 = canvas.coords(ball)
    
    # 벽에 부딪혔는지 확인하고 방향 바꾸기
    # 왼쪽 벽(x1 <= 0) 또는 오른쪽 벽(x2 >= 400)에 부딪히면
    if x1 <= 0 or x2 >= 400:
        dx = -dx                # x방향 이동을 반대로 바꿈
    
    # 위쪽 벽(y1 <= 0) 또는 아래쪽 벽(y2 >= 300)에 부딪히면
    if y1 <= 0 or y2 >= 300:
        dy = -dy                # y방향 이동을 반대로 바꿈
    
    # 공을 새로운 위치로 이동
    # move(): 객체를 지정한 거리만큼 이동시키는 함수
    canvas.move(ball, dx, dy)
    
    # 50밀리초(0.05초) 후에 이 함수를 다시 실행
    # after(): 지정한 시간 후에 함수를 실행하는 함수
    root.after(50, move_ball)


# 공 움직이기 시작
move_ball()

# 윈도우를 화면에 표시하고 프로그램 실행
# mainloop(): 윈도우를 계속 띄워두고 사용자의 행동을 기다리는 함수
root.mainloop()

# 🎯 연습과제들 (아래 숫자를 바꿔보세요!)
#
# 📝 연습과제 1: 공 크기 바꿔보기
# - ball = canvas.create_oval(50, 50, 100, 100, fill="red")  # 더 큰 공
# - ball = canvas.create_oval(50, 50, 70, 70, fill="red")    # 더 작은 공
#
# 📝 연습과제 2: 공 속도 바꿔보기
# - dx, dy = 8, 6    # 더 빠른 속도
# - dx, dy = 2, 1    # 더 느린 속도
# - dx, dy = 10, 2   # 가로로만 빠른 속도
#
# 📝 연습과제 3: 공 색상 바꿔보기
# - fill="blue"      # 파란 공
# - fill="green"     # 초록 공
# - fill="purple"    # 보라 공
#
# 📝 연습과제 4: 애니메이션 속도 바꿔보기
# - root.after(30, move_ball)   # 더 빠른 애니메이션 (30ms)
# - root.after(100, move_ball)  # 더 느린 애니메이션 (100ms)
#
# 📝 연습과제 5: 캔버스 크기 바꿔보기
# - Canvas(root, width=500, height=400, bg="white")  # 더 큰 공간
# - Canvas(root, width=200, height=150, bg="white")  # 더 작은 공간
# - 벽 충돌 조건도 함께 바꿔야 함: if x2 >= 500, if y2 >= 400
