import collections

def solution(participant, completion):
    dic = collections.Counter(participant)

    for i in completion:
        dic[i] -= 1
    
    for i, j in dic.items():
        if( j == 1 ): return i

#새로 배운 점
'''
1. collections모듈
	1-1. Counter함수 : 중복 값을 카운트하고 딕셔너리 형태로 리턴해준다.
2. dict.items()는 딕셔너리의 키와 값을 함께 리스트로 리턴해준다.
'''
