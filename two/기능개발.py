def solution(progresses, speeds):
    answer = []
    day = 0
    while ( progresses ):
        #진도율 증가
        for i in range(len(progresses)):
            if( progresses[i] < 100 ):
                progresses[i] += speeds[i]

        #앞에서 부터 100이 넘은 애들은 pop을 함과 동시에 배포 카운트
        if( progresses and progresses[0] >= 100 ):
            answer.append(0)
            while( progresses and progresses[0] >= 100 ):
                progresses.pop(0)
                speeds.pop(0)
                answer[day] += 1
            day += 1
        
    return answer

'''
새로 배운 점
1. while문과 pop을 동시에 쓸 경우 while문의 조건을 주의하자
'''