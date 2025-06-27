# flake8: noqa
# pylint: disable=wildcard-import,unused-wildcard-import,undefined-variable
# 02. 기본 이동과 회전 연습
# forward, left 명령어를 사용해서 정사각형을 그려봅시다

from turtle import *

print("🐢 기본 이동과 회전 - 정사각형 그리기")
print("거북이가 이동하면서 정사각형을 그리는 모습을 확인해주세요!")

# 거북이 객체 생성 - 필요 없어짐

# 거북이 속도 설정
speed(1)

# 정사각형 그리기 (한 변씩 직접 그리기)
print("1번째 변 그리기...")
forward(100)   # 앞으로 100만큼
left(90)       # 왼쪽으로 90도 회전

print("2번째 변 그리기...")
forward(100)   # 다시 앞으로 100만큼
left(90)       # 또 왼쪽으로 90도

print("3번째 변 그리기...")
forward(100)
left(90)

print("4번째 변 그리기...")
forward(100)
left(90)

print("✅ 정사각형 완성!")
print("반복문을 사용하면 더 간단하게 만들 수 있어요!")

# 잠시 기다리기
done() 