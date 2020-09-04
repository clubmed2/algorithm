def solution(priorities, location):
    answer = 0
    priorities = list(zip(range(len(priorities)), priorities))

    while(priorities):
        temp = priorities.pop(0)
        for i in range(0, len(priorities)):
            if(temp[1] < priorities[i][1]):
                priorities.append(temp)
                break
        else:
            answer += 1
            if(temp[0] == location):
                return answer


'''
새로 배운 점
1. collections.deque를 사용하자
'''
