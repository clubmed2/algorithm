import math


def solution(n):
    isPrime = [False, False] + [True]*(n-1)

    for i in range(2, int(math.sqrt(n))+1):
        if(isPrime[i] == True):
            for k in range(i*2, n+1, i):
                isPrime[k] = False
    answer = isPrime.count(True)
    return answer


# 새로 배운 점
'''
1. 에라토스테네스 체
'''
