def solution(arr, divisor):
    answer = []

    for i in arr:
        if(i % divisor == 0):
            answer.append(i)
    if(answer == []):
        answer.append(-1)
    answer.sort()
    return answer


# 새로 배운 점
'''
1. 없음
'''
