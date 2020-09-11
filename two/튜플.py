import re


def solution(s):
    a = re.split("},{", s[2:-2])
    b = []
    answer = []

    for i in a:
        b.append(i.split(','))
    b.sort(key=len)
    for i in b:
        for j in i:
            if(int(j) not in answer):
                answer.append(int(j))
    return answer


# 새로 배운 점
'''
1. 비교하여 포함여부를 결정할 때 저장된 배열과 비교하자.
'''
