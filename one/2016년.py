from datetime import datetime


def solution(a, b):
    week = "FRI,SAT,SUN,MON,TUE,WED,THU".split(',')
    day1 = datetime(2016, 1, 1)
    day2 = datetime(2016, a, b)
    return week[(day2-day1).days % 7]


# 새로 배운 점
'''
1. 문제에 문자열이 주어졌을 때 split을 사용하여 리스트로 만들면 빠르다.
2. datetime(2016,1,1).weekday()하면 요일을 구할 수 있다.
'''
