def solution(s):
    result = []

    for i in s:
        result.append(i)
        if(len(result) > 1 and result[-1] == result[-2]):
            result.pop()
            result.pop()
    return 1 if result == [] else 0


# 새로 배운 점
'''
1. 없음
'''
