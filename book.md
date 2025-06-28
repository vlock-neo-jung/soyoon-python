# 파이썬 리스트 완전정복

## 공백 리스트에서 추가하기

```python
>>> heroes = []
>>> heroes.append("아이언맨")
>>> print(heroes)
['아이언맨']

>>> heroes.append("닥터 스트레인지")
>>> print(heroes)
['아이언맨', '닥터 스트레인지']
```

## 점의 의미

- 파이썬에서 모든 것은 객체(object)이다. 객체는 관련된 변수와 함수를 묶은 것이다.
- 리스트도 객체이며, 객체 안에 있는 무언가를 사용할 때는 `객체이름.함수이름` 형태로 사용한다.

**예시**
```python
heroes.append("아이언맨")
```

## 리스트 항목 접근하기

```python
>>> letters = ['A', 'B', 'C', 'D', 'E', 'F']

>>> print(letters[0])
A
>>> print(letters[1])
B
>>> print(letters[-4])
C
```

## 슬라이싱

- 슬라이싱(slicing)은 리스트에서 여러 항목을 한 번에 추출하는 방법이다.

```python
>>> letters = ['A', 'B', 'C', 'D', 'E', 'F']
>>> print(letters[0:3])
['A', 'B', 'C']
```

## 인덱스 생략

```python
>>> letters = ['A', 'B', 'C', 'D', 'E', 'F']

>>> print(letters[:3])
['A', 'B', 'C']

>>> print(letters[3:])
['D', 'E', 'F']

>>> print(letters[:])
['A', 'B', 'C', 'D', 'E', 'F']
```

## 리스트 항목 변경하기

```python
>>> heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
>>> heroes[1] = "닥터 스트레인지"
>>> print(heroes)
['아이언맨', '닥터 스트레인지', '헐크', '스칼렛 위치']
```

## 함수를 이용하여 추가하기

```python
>>> heroes.append("스파이더맨")
>>> print(heroes)
['아이언맨', '닥터 스트레인지', '헐크', '스칼렛 위치', '스파이더맨']

>>> heroes.insert(1, "배트맨")
>>> print(heroes)
['아이언맨', '배트맨', '닥터 스트레인지', '헐크', '스칼렛 위치', '스파이더맨']
```

## 항목 삭제하기

```python
heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
heroes.remove("스칼렛 위치")
print(heroes)
['아이언맨', '토르', '헐크']
```

## 항목이 리스트 안에 있는지 체크

```python
if "헐크" in heroes:
    heroes.remove("헐크")
print(heroes)
['아이언맨', '토르']
```

## del로 삭제하기 (인덱스 사용)

```python
heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
del heroes[0]
print(heroes)
['토르', '헐크', '스칼렛 위치']
```

## 리스트 탐색하기 (index 사용)

```python
heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
print(heroes.index("토르"))
1
```

## 리스트 방문하기

```python
heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
for hero in heroes:
    print(hero)
```

**출력**
```
아이언맨
토르
헐크
스칼렛 위치
```

## 리스트 정렬하기

```python
heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
heroes.sort()
print(heroes)
['스칼렛 위치', '아이언맨', '토르', '헐크']
```

---

# 선택구조 - if 조건문

## 기본 구조

### 기본 구조
```python
if 조건식:
    문장1
else:
    문장2
```

### 다중 조건
```python
if 조건식1:
    문장1
elif 조건식2:
    문장2
else:
    문장3
```

### 다중 elif 예시
```python
if 조건식1:
    문장1
elif 조건식2:
    문장2
elif 조건식3:
    문장3
else:
    문장4
```

## if-else 조건문: 합격/불합격 판별

```python
score = int(input("성적을 입력하세요: "))
if score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")
```

## if-else 조건문: 홀수/짝수 판별

```python
score = int(input("숫자를 입력하세요: "))
if score % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
```

## if-else 조건문: 나이에 따른 영화 관람 판별

```python
age = int(input("나이를 입력하세요: "))
if age >= 19:
    print("통과")
else:
    print("집으로.")
```

## if-else 조건문: 양수, 음수, 0 판별

```python
number = int(input("숫자를 입력하세요: "))
if number > 0:
    print("양수입니다")
elif number < 0:
    print("음수입니다")
else:
    print("0입니다")
```

## if-else 조건문: 점수에 따른 등급 출력

```python
number = int(input("점수를 입력하세요: "))
if number >= 90:
    print("A입니다")
elif number >= 80:
    print("B입니다")
else:
    print("C입니다")
```

---

# FOR문과 WHILE문 (반복문)

## 기본 for 반복문

```python
for 변수 in range(숫자):
    문장1
    문장2
```

- 변수는 0부터 숫자-1까지 1씩 증가하면서 문장1, 문장2를 실행

```python
for 변수 in range(5):
    문장1
```

## for 반복문 - 시작값과 끝값

```python
for 변수 in range(숫자1, 숫자2):
    문장1
    문장2
```

- 변수는 숫자1부터 숫자2-1까지 1씩 증가

```python
for 변수 in range(1, 6):
    문장1
```

## for 반복문 - 시작, 끝, 증감

```python
for 변수 in range(시작, 끝, 증감):
    문장1
    문장2
```

- 변수는 시작부터 끝-1까지 증감만큼 증가

```python
for 변수 in range(1, 10, 2):
    문장1
```

## while 반복문 (조건 반복)

```python
while 조건식:
    문장1
```

- 조건식이 참인 동안 문장1 반복 실행, 거짓이면 탈출

## for 반복문 예제 (반복횟수 아는 경우)

```python
for i in range(5):
    print("방문을 환영합니다!")
```

**출력**
```
방문을 환영합니다!
방문을 환영합니다!
방문을 환영합니다!
방문을 환영합니다!
방문을 환영합니다!
```

## 별 출력 (for문)

```python
for i in range(1, 9):
    print("★" * i)
```

## 별 출력 (while문)

```python
i = 1
while i <= 8:
    print('★' * i)
    i += 1
```

## 구구단 출력

```python
dan = int(input("원하는 단을 입력하세요: "))
for i in range(1, 10):
    print(dan, "*", i, "=", dan * i)
```

## 1부터 100까지 합계 출력 (for)

```python
sum = 0
for i in range(1, 101):
    sum += i
print("1부터 100까지 합은", sum, "입니다.")
```

## 1부터 100까지 합계 출력 (while)

```python
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print("1부터 100까지의 합은", sum, "입니다.")
```

## 1부터 10까지 짝수 출력 (for / while)

```python
for i in range(2, 11, 2):
    print(i, end=" ")
print()

a = 0
while a < 10:
    a += 2
    print(a, end=" ")
```

## 50까지 5의 배수 출력

```python
for i in range(5, 51, 5):
    print(i, end=" ")
print()

i = 1
while i <= 50:
    if i % 5 == 0:
        print(i, end=" ")
    i += 1
```

---

# 중첩제어 (다중 FOR문)

## 구구단 출력 (2단 ~ 9단)

```python
for x in range(2, 10):
    for y in range(1, 10):
        print(x, "*", y, "=", x * y, end=" ")
    print()
```

## 사선으로 별 출력

```python
for x in range(1, 8):
    for y in range(1, 8):
        if x == y:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

## 역삼각형 별 출력

```python
for x in range(1, 8):
    for y in range(1, 8):
        if x <= y:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

---

# 🐢 파이썬 Turtle 모듈

## Turtle 모듈 기본 기능

| 기능 | 사용법 예시 | 설명 |
|------|-------------|------|
| 앞으로 이동 | `forward(이동거리)` | 거북이가 앞으로 이동 |
| 뒤로 이동 | `backward(이동거리)` | 거북이가 뒤로 이동 |
| 오른쪽 회전 | `right(각도)` | 시계 방향으로 회전 |
| 왼쪽 회전 | `left(각도)` | 반시계 방향으로 회전 |
| 선 굵기 설정 | `pensize(굵기)` | 선 굵기 설정 |
| 거북이 모양 변경 | `shape('turtle')`, `'arrow'` 등 | 거북이의 커서 모양 지정 |
| 배경색 설정 | `bgcolor('pink')` | 배경색 설정 |
| 선 색 & 채우기 색 | `color('blue', 'yellow')` | 첫 번째는 선 색, 두 번째는 채우기 색 |
| 채우기 시작/끝 | `begin_fill()`, `end_fill()` | 다각형 내부를 색으로 채우기 시작/끝 |
| 펜 들어올리기/내리기 | `penup()`, `pendown()` | 이동할 때 선을 그릴지 여부 설정 |
| 점 찍기 | `dot(크기)` | 원 모양의 점 그리기 |
| 속도 설정 | `speed(0~10)` | 0은 가장 빠름 |

## 🔺 삼각형 그리기

```python
from turtle import *
for i in range(3):
    forward(100)
    left(120)
```

## 🔺 삼각형 색상/모양 설정

```python
from turtle import *
shape("turtle")
color("blue", "yellow")
bgcolor("pink")
begin_fill()
for i in range(3):
    forward(200)
    left(120)
end_fill()
```

## 🔷 다각형 그리기 (사용자 입력)

```python
from turtle import *
n = int(textinput("질문1", "원하는 다각형은?"))
for i in range(n):
    forward(100)
    left(360 / n)
```

## 🟥 채워진 정사각형 그리기

```python
from turtle import *
color("blue", "pink")
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()
exitonclick()  # 클릭 시 창 종료
```

## 🟢 원 반복해서 패턴 그리기

```python
from turtle import *
n = 50
bgcolor("black")
color("green")
speed(0)
for i in range(n):
    circle(80)
    left(360 / n)
```

## 🌀 무늬 그리기 (선으로 반복)

```python
from turtle import *
shape("turtle")
speed('fastest')
color("pink")
for i in range(300):
    forward(i)
    right(91)
```

## ⭐ 별 그리기

```python
from turtle import *
shape("turtle")
color("blue", "pink")
speed(0)
bgcolor("yellow")
bgpic("sky1.gif")  # 배경 이미지 (있을 경우)
begin_fill()
pensize(1)
for i in range(5):
    forward(150)
    right(144)
end_fill()
```

## 🌸 꽃잎 무늬 원 반복

```python
from turtle import *
begin_fill()
color("pink")
for i in range(6):
    circle(50, 220)  # 반지름 50, 220도까지 원 그리기
    left(200)
end_fill()
```
