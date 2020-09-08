def fibo(answer, depth):
    if(depth == 1):
        return 1
    if(depth == 0):
        return 0
    return fibo(answer, depth-1) + fibo(answer, depth-2)


def solution(n):
    answer = []

    return fibo(answer, n) % 1234567
    # for i in range(2, n+1):
    #     answer.append(answer[i-2]+answer[i-1])
    # return answer[n] % 1234567


# 새로 배운 점
'''
1.  재귀는 빠르지 않다.
'''
