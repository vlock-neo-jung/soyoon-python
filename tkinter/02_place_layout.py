"""
tkinter의 place() 메소드를 사용한 위젯 배치 예제
- place(): 정확한 x, y 좌표로 위젯의 위치를 지정하는 방법
- 픽셀 단위로 정확한 위치 지정이 가능합니다
"""

# tkinter 라이브러리 불러오기 (GUI 윈도우를 만들기 위해 필요)
import tkinter as tk

# 윈도우(창) 객체 생성
# tk.Tk(): 새로운 윈도우를 만드는 함수
window = tk.Tk()

# 윈도우 제목 설정
# title(): 윈도우 상단에 보이는 제목을 설정하는 함수
window.title("Place Example")

# 윈도우 크기 설정 (가로 x 세로, 픽셀 단위)
# geometry(): 윈도우의 크기를 설정하는 함수
window.geometry("300x200")

# 첫 번째 버튼 생성
# Button(): 클릭할 수 있는 버튼을 만드는 함수
# bg: background(배경색)의 줄임말
btn1 = tk.Button(
    window,                    # 어느 윈도우에 버튼을 넣을지
    text="버튼 1",             # 버튼에 표시될 글자
    bg="lightblue"             # 버튼의 배경색
)

# 첫 번째 버튼을 정확한 좌표에 배치
# place(): x, y 좌표를 이용해 위젯의 위치를 정확히 지정하는 함수
# x=50: 왼쪽에서 50픽셀 떨어진 위치
# y=50: 위쪽에서 50픽셀 떨어진 위치
btn1.place(x=50, y=50)

# 두 번째 버튼 생성
btn2 = tk.Button(
    window,
    text="버튼 2",
    bg="lightgreen"            # 다른 색상으로 설정
)

# 두 번째 버튼을 다른 좌표에 배치
btn2.place(x=150, y=50)

# 세 번째 버튼 생성
btn3 = tk.Button(
    window,
    text="버튼 3",
    bg="lightcoral"            # 또 다른 색상으로 설정
)

# 세 번째 버튼을 또 다른 좌표에 배치
btn3.place(x=100, y=100)

# 윈도우를 화면에 표시하고 프로그램 실행
# mainloop(): 윈도우를 계속 띄워두고 사용자의 행동을 기다리는 함수
window.mainloop()

# 🎯 연습과제들 (아래 숫자를 바꿔보세요!)
#
# 📝 연습과제 1: 버튼 위치 바꿔보기
# - btn1.place(x=30, y=30)  # 첫 번째 버튼을 왼쪽 위로
# - btn2.place(x=200, y=80) # 두 번째 버튼을 오른쪽으로
# - btn3.place(x=120, y=150) # 세 번째 버튼을 아래쪽으로
#
# 📝 연습과제 2: 버튼 색상 바꿔보기
# - bg="yellow"    # 노란색
# - bg="pink"      # 분홍색
# - bg="orange"    # 주황색
# - bg="purple"    # 보라색
#
# 📝 연습과제 3: 버튼 텍스트 바꿔보기
# - text="클릭!"   # 다른 글자로 변경
# - text="눌러요"  # 한글로 변경
# - text="Button"  # 영어로 변경
#
# 📝 연습과제 4: 윈도우 크기 바꿔보기
# - window.geometry("400x300")  # 더 큰 창으로
# - window.geometry("250x150")  # 더 작은 창으로
