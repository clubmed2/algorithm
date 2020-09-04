def solution(strings, n):
    strings.sort()
    answer = sorted(strings, key=lambda x: (x[n]))
    return answer


# 새로 배운 점
'''
1. sorted에 key를 줄 수 있다. lambda를 사용해 strings를 x로 받아 x[n]의 값들을 기준으로 정렬한다.
'''
