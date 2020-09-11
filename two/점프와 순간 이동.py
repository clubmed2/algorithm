def solution(n):
    answer = 1  # 첫 칸은 에너지 사용

    while(n != 1):
        if(n & 1 == 1):
            answer += 1
        n //= 2
    return answer


# 새로 배운 점
'''
1. 없음
'''
