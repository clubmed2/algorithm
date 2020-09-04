def solution(s):
    s = s.lower()
    answer = True if s.count('p') == s.count('y') else False
    return answer

#새로 배운 점
'''
1. string를 list로 변환하지 않아도 count가 가능하다.
'''        