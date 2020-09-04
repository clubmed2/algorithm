def solution(array, commands):
    answer = []
    
    for i in commands:
        answer.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
    return answer

#새로 배운 점
'''
1. sorted()는 새로운 리스트를 리턴하고, .sort()는 리턴하지 않는다.
'''    