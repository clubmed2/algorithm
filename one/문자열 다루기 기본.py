def solution(s):
    answer = len(s) in (4, 6) and s.isdigit() == True
    return answer


# 새로 배운 점
'''
1. string를 list로 변환하지 않아도 count가 가능하다.
2. isdecimal()이 좀 더 정확하다.
'''
