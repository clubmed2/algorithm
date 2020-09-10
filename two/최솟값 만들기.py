def solution(A, B):
    sum = 0
    A.sort(reverse=True)
    B.sort()

    for i in range(len(A)):
        sum += A.pop()*B.pop()
    return sum


# 새로 배운 점
'''
1. 없음
'''
