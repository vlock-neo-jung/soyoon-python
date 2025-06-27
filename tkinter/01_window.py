"""
tkinter를 사용한 간단한 색깔 바꾸기 프로그램
- 버튼을 클릭하면 윈도우 배경색이 랜덤하게 바뀝니다
- tkinter: 파이썬에서 GUI(그래픽 사용자 인터페이스)를 만들 수 있는 라이브러리
"""

# tkinter 라이브러리 불러오기 (GUI 윈도우를 만들기 위해 필요)
import tkinter as tk
# random 라이브러리 불러오기 (랜덤한 색상을 선택하기 위해 필요)
import random

# 사용할 색상들을 리스트에 저장
# 리스트: 여러개의 데이터를 순서대로 담을 수 있는 자료형
colors = ["red", "blue", "green", "yellow", 
          "purple", "orange", "pink", "white"]

# 윈도우(창) 객체 생성
# tk.Tk(): 새로운 윈도우를 만드는 함수
window = tk.Tk()

# 윈도우 제목 설정
# title(): 윈도우 상단에 보이는 제목을 설정하는 함수
window.title("색깔 바꾸기 버튼!")

# 윈도우 크기 설정 (가로 x 세로, 픽셀 단위)
# geometry(): 윈도우의 크기를 설정하는 함수
window.geometry("300x200")


# 색상을 바꾸는 함수 정의
# def: 함수를 만들 때 사용하는 키워드
def change_color():
    """버튼을 클릭했을 때 실행되는 함수"""
    # random.choice(): 리스트에서 랜덤하게 하나를 선택하는 함수
    random_color = random.choice(colors)
    # configure(): 윈도우의 설정을 바꾸는 함수
    # bg: background(배경)의 줄임말
    window.configure(bg=random_color)


# 버튼 객체 생성
# Button(): 클릭할 수 있는 버튼을 만드는 함수
button = tk.Button(
    window,                    # 어느 윈도우에 버튼을 넣을지
    text="색 바꾸기",           # 버튼에 표시될 글자
    command=change_color,      # 버튼을 클릭했을 때 실행할 함수
    font=("Arial", 15)         # 글자체와 크기 설정
)

# 버튼을 윈도우에 배치
# pack(): 위젯을 윈도우에 배치하는 함수
# pady: 위아래 여백을 설정 (픽셀 단위)
button.pack(pady=70)

# 윈도우를 화면에 표시하고 프로그램 실행
# mainloop(): 윈도우를 계속 띄워두고 사용자의 행동을 기다리는 함수
window.mainloop()

"""
🎯 연습과제들 (아래 숫자를 바꿔보세요!)

📝 연습과제 2: 윈도우 크기나 제목 바꿔보기
- 제목 바꾸기: window.title("여기에 새로운 제목") 
- 크기 바꾸기: window.geometry("400x300") 또는 다른 숫자로

📝 연습과제 3: 버튼 텍스트나 폰트 크기 변경해보기  
- 버튼 글자 바꾸기: text="여기에 새로운 글자"
- 폰트 크기 바꾸기: font=("Arial", 20) 또는 다른 숫자로

📝 연습과제 4: 버튼 위치(pady 값) 조정해보기
- 버튼을 위로: pady=30 (작은 숫자)
- 버튼을 아래로: pady=100 (큰 숫자)
"""

