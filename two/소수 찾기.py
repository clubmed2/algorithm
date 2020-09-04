from itertools import permutations
import collections


def solution(numbers):
    primes = []
    answer = 0

    for i in range(1, len(numbers)+1):
        for j in list(permutations(numbers, i)):
            j = ''.join(list(j)).lstrip('0')
            primes.append(j)

    for i in list(collections.Counter(primes)):
        if(i != '' and i != '1'):
            for j in range(2, int(int(i)**(1/2))+1):
                if(int(i) % j == 0):
                    break
            else:
                answer += 1
    return answer


# 새로 배운 점
'''
1. itertools.permutations, itertools.combinations
'''
