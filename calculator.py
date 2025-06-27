# calculator.py - 간단한 계산기 모듈


def add(a, b):
    """두 수를 더하는 함수"""
    return a + b


def subtract(a, b):
    """두 수를 빼는 함수"""
    return a - b


def multiply(a, b):
    """두 수를 곱하는 함수"""
    return a * b


def divide(a, b):
    """두 수를 나누는 함수"""
    if b == 0:
        return "0으로 나눌 수 없습니다!"
    return a / b


def square(a):
    """수의 제곱을 구하는 함수"""
    return a * a


def average(numbers):
    """숫자 리스트의 평균을 구하는 함수"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers) 