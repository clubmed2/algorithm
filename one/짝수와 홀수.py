def solution(num):
    answer = "Even" if num & 1 == 0 else "Odd"
    return answer


# 새로 배운 점
'''
1. num%2==0말고 num&1==0로 할 수도 있다.
'''
