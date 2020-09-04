def solution(n):
    answer = list(map(int, reversed(str(n))))
    return answer


# 새로 배운 점
'''
1. reversed(), .reverse()
2. str타입에 reversed(), sorted() 등을 사용하면 list로 반환해준다.
'''
