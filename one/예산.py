def solution(d, budget):
    answer = 0
    while( d != [] and budget >= min(d) ):
        budget -= min(d)
        d.remove(min(d))
        answer += 1
    return answer

#새로 배운 점
'''
1. 없음
'''  