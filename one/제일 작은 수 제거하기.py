def solution(arr):
    arr.remove(min(arr))
    if(arr == []):
        answer = [-1]
    else:
        answer = arr
    return answer


# 새로 배운 점
'''
1. remove는 리턴값이 없다.
'''
