def solution(N, stages):
    answer = {}
    success = len(stages) #첫 라운드는 모든 플레이어가 무조건 도달했다.
    for i in range(1,N+1):
        fail = stages.count(i)
        if( fail == 0 ):
            answer[i] = 0
        else:
            answer[i] = fail/(fail+success)
            
        success -= fail #클리어하지 못한 플레이어는 이 이상 스테이지부터 도달한 플레이어에서 빠진다.
            
    #answer = [ i[0] for i in sorted(answer.items(), key = lambda x: x[1], reverse=True) ]
    answer = sorted(answer, key = lambda x: answer[x], reverse=True)
        
    return answer

#새로 배운 점
'''
1. 딕셔너리 정렬
2. 특정 문자를 찾을 땐 count를 사용하자
'''  