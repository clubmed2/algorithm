def solution(n):
    answer = 0
    for i in range(1, int(n/2)+1):
        if(n % i == 0):
            answer += i
    answer += n
    return answer


# 새로 배운 점
'''
1. 없음
'''
