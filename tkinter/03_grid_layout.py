"""
tkinter의 grid() 메소드를 사용한 위젯 배치 예제
- grid(): 표 형태의 격자로 위젯을 정렬하는 방법
- row(행)와 column(열)으로 위치를 지정합니다
"""

# tkinter 라이브러리 불러오기 (GUI 윈도우를 만들기 위해 필요)
import tkinter as tk

# 윈도우(창) 객체 생성
# tk.Tk(): 새로운 윈도우를 만드는 함수
window = tk.Tk()

# 윈도우 제목 설정
# title(): 윈도우 상단에 보이는 제목을 설정하는 함수
window.title("맛집 Grid Example")

# 윈도우 크기 설정 (가로 x 세로, 픽셀 단위)
# geometry(): 윈도우의 크기를 설정하는 함수
window.geometry("300x200")

# 첫 번째 버튼 생성 (0행 0열에 배치할 예정)
# Button(): 클릭할 수 있는 버튼을 만드는 함수
btn1 = tk.Button(
    window,                    # 어느 윈도우에 버튼을 넣을지
    text="버튼 1",             # 버튼에 표시될 글자
    bg="lightblue",            # 버튼의 배경색
    fg="white",                # 글자색 (foreground)
    font=("Arial", 12, "bold")  # 글자체, 크기, 스타일
)

# 첫 번째 버튼을 격자의 0행 0열에 배치
# grid(): 표 형태로 위젯을 배치하는 함수
# row=0: 첫 번째 행 (맨 위)
# column=0: 첫 번째 열 (맨 왼쪽)
# padx, pady: 버튼 주변의 여백 설정
btn1.grid(row=0, column=0, padx=10, pady=10)

# 두 번째 버튼 생성 (0행 1열에 배치할 예정)
btn2 = tk.Button(
    window,
    text="버튼 2",
    bg="lightgreen",           # 다른 색상으로 설정
    fg="white",
    font=("Arial", 12, "bold")
)

# 두 번째 버튼을 0행 1열에 배치 (첫 번째 버튼 오른쪽)
btn2.grid(row=0, column=1, padx=10, pady=10)

# 세 번째 버튼 생성 (1행 0열에 배치할 예정)
btn3 = tk.Button(
    window,
    text="버튼 3",
    bg="lightcoral",           # 또 다른 색상으로 설정
    fg="white",
    font=("Arial", 12, "bold")
)

# 세 번째 버튼을 1행 0열에 배치 (첫 번째 버튼 아래)
btn3.grid(row=1, column=0, padx=10, pady=10)

# 네 번째 버튼 생성 (1행 1열에 배치할 예정)
btn4 = tk.Button(
    window,
    text="버튼 4",
    bg="gold",                 # 금색으로 설정
    fg="white",
    font=("Arial", 12, "bold")
)

# 네 번째 버튼을 1행 1열에 배치 (두 번째 버튼 아래, 세 번째 버튼 오른쪽)
btn4.grid(row=1, column=1, padx=10, pady=10)

# 윈도우를 화면에 표시하고 프로그램 실행
# mainloop(): 윈도우를 계속 띄워두고 사용자의 행동을 기다리는 함수
window.mainloop()

# 🎯 연습과제들 (아래 숫자를 바꿔보세요!)
#
# 📝 연습과제 1: 버튼 위치 바꿔보기 (격자 배치)
# - btn1.grid(row=0, column=1, padx=10, pady=10)  # 첫 번째 버튼을 오른쪽으로
# - btn2.grid(row=1, column=0, padx=10, pady=10)  # 두 번째 버튼을 아래로
# - btn3.grid(row=0, column=0, padx=10, pady=10)  # 세 번째 버튼을 맨 위로
#
# 📝 연습과제 2: 여백(padding) 조정하기
# - padx=20, pady=20  # 더 큰 여백
# - padx=5, pady=5    # 더 작은 여백
# - padx=30, pady=5   # 가로만 큰 여백
#
# 📝 연습과제 3: 버튼 색상과 글자 바꿔보기
# - bg="purple", fg="yellow"  # 보라 배경에 노란 글자
# - bg="navy", fg="white"     # 남색 배경에 흰 글자
# - text="새버튼"             # 다른 텍스트로 변경
#
# 📝 연습과제 4: 폰트 크기 바꿔보기
# - font=("Arial", 15, "bold")  # 더 큰 글자
# - font=("Arial", 10, "bold")  # 더 작은 글자
# - font=("Arial", 12, "italic") # 기울임 글자
