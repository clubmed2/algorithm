def solution(n):
    answer = bin(n)[2:].count('1')
    idx = 1

    while(answer != bin(n+idx)[2:].count('1')):
        idx += 1
    return n+idx


# 새로 배운 점
'''
1. 없음
'''
