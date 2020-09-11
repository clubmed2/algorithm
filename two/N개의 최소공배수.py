import math


def solution(n):
    n.sort()

    for k in range(len(n)-1):
        i = n.pop()
        j = n.pop()
        yak = math.gcd(i, j)
        bae = int(i*j / yak)
        n.append(bae)
    return n[0]


# 새로 배운 점
'''
1. 2개 이상인 수 집합의 최소공배수는 제일 큰 수부터
2. math.gcd(): 최대공약수
'''
