def solution(num):
    if(num == 1):
        return
    for i in range(500):
        num = int(num/2) if num % 2 == 0 else num*3+1
        if(num == 1):
            return i+1
    return -1


# 새로 배운 점
'''
1. num=1인 경우, 즉 if조건이 시작하자마자 걸리는 경우를 생각하자.
'''
