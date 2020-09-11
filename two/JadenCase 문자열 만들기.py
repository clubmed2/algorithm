def solution(s):
    answer = ""
    
    for i in s.split(' '):
        if(i == ''):
            answer += " "
        else:
            answer += i[0].upper()+i[1:].lower()+" "
    return answer[:-1]


# 새로 배운 점
'''
1. split()할 때 공백 개수 고려
'''
