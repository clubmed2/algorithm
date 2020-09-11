from itertools import combinations


def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    result = list(map(sum, (list(combinations(nums, 3)))))

    return sum(list(map(isPrime, result)))


# 새로 배운 점
'''
1. 없음
'''
