"""
tkinter를 사용한 이미지 움직이기 애니메이션 예제
- Canvas에 이미지를 넣고 자동으로 움직이게 하는 프로그램
- 이미지 파일이 필요합니다 (예: '1.png')
- 이미지가 없어도 실행되며, 대신 사각형으로 대체됩니다
"""

# tkinter 라이브러리 불러오기 (GUI 윈도우를 만들기 위해 필요)
import tkinter as tk

# 윈도우(창) 객체 생성
# tk.Tk(): 새로운 윈도우를 만드는 함수
root = tk.Tk()

# Canvas 객체 생성 (이미지가 움직일 공간)
# Canvas: 그림을 그리고 애니메이션을 만들 수 있는 도화지
canvas = tk.Canvas(
    root,                      # 어느 윈도우에 캔버스를 넣을지
    width=500,                 # 캔버스 가로 크기
    height=500                 # 캔버스 세로 크기
)

# 캔버스를 윈도우에 배치
canvas.pack()

# 이미지 로드 시도 (이미지 파일이 있는 경우)
try:
    # PhotoImage(): 이미지 파일을 불러오는 함수
    # file: 불러올 이미지 파일 이름 (예: '1.png')
    image = tk.PhotoImage(file="tkinter/1.png")
    
    # 이미지를 캔버스에 추가
    # create_image(): 캔버스에 이미지를 넣는 함수
    # anchor=tk.NW: 이미지의 왼쪽 위 모서리를 기준점으로 설정
    img_id = canvas.create_image(
        50, 50,                # 이미지가 표시될 위치 (x=50, y=50)
        anchor=tk.NW,          # 앵커 포인트 (NorthWest = 왼쪽 위)
        image=image            # 표시할 이미지 객체
    )
    
    using_image = True         # 이미지 사용 성공 표시
    
except FileNotFoundError:
    # 이미지 파일이 없으면 사각형으로 대체
    print("이미지 파일 '1.png'를 찾을 수 없어서 사각형으로 대체합니다.")
    
    # 사각형 생성 (이미지 대신)
    img_id = canvas.create_rectangle(
        50, 50,                # 사각형의 왼쪽 위 모서리
        100, 100,              # 사각형의 오른쪽 아래 모서리
        fill="blue"            # 사각형 색상
    )
    
    using_image = False        # 이미지 대신 사각형 사용 표시


# 이미지(또는 사각형)를 움직이는 함수 정의
def animate_image():
    """이미지를 오른쪽으로 5픽셀씩 움직이는 함수"""
    
    # 객체를 오른쪽으로 10픽셀, 아래로 0픽셀 이동
    # move(객체, x이동거리, y이동거리): 객체를 지정한 거리만큼 이동
    canvas.move(img_id, 10, 0)
    
    # 50밀리초(0.05초) 후에 이 함수를 다시 실행
    # after(): 지정한 시간 후에 함수를 실행하는 함수 (반복 실행)
    root.after(50, animate_image)


# 애니메이션 시작
animate_image()

# 윈도우를 화면에 표시하고 프로그램 실행
# mainloop(): 윈도우를 계속 띄워두고 사용자의 행동을 기다리는 함수
root.mainloop()

"""
🎯 연습과제들 (아래 숫자를 바꿔보세요!)

📝 연습과제 1: 이미지 이동 방향 바꿔보기
- canvas.move(img_id, 0, 10)   # 아래쪽으로 움직이기
- canvas.move(img_id, -5, 0)   # 왼쪽으로 움직이기  
- canvas.move(img_id, 5, 5)    # 오른쪽 아래 대각선으로

📝 연습과제 2: 이동 속도 바꿔보기
- canvas.move(img_id, 15, 0)   # 더 빠르게 이동
- canvas.move(img_id, 3, 0)    # 더 느리게 이동
- canvas.move(img_id, 20, 0)   # 아주 빠르게 이동

📝 연습과제 3: 애니메이션 속도 바꿔보기
- root.after(30, animate_image)  # 더 빠른 애니메이션 (30ms)
- root.after(100, animate_image) # 더 느린 애니메이션 (100ms)
- root.after(20, animate_image)  # 아주 빠른 애니메이션 (20ms)

📝 연습과제 4: 시작 위치 바꿔보기
- 이미지: canvas.create_image(100, 100, anchor=tk.NW, image=image)
- 사각형: canvas.create_rectangle(100, 100, 150, 150, fill="blue")

📝 연습과제 5: 사각형 색상 바꿔보기 (이미지가 없는 경우)
- fill="red"       # 빨간 사각형
- fill="green"     # 초록 사각형
- fill="purple"    # 보라 사각형

💡 팁: 이미지 파일을 사용하려면 같은 폴더에 '1.png' 파일을 넣어주세요!
""" 