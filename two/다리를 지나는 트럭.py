def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = []
    
    wait = len(truck_weights)
    done = 0
    
    while( done != wait ):
        answer += 1
        #들어올 수 있으면 들어와
        if( truck_weights and sum([onBridge[i][0] for i in range(len(onBridge))]) + truck_weights[0] <= weight ):
            onBridge.append([truck_weights[0], 0])
            truck_weights.pop(0)
        #한 칸씩 이동
        for i in range(len(onBridge)):
            onBridge[i][1] += 1
        #나갈때가 됐는지
        if( onBridge[0][1] == bridge_length ):
            onBridge.pop(0)
            done += 1
    
    answer += 1
    return answer

#새로 배운 점
'''
1. while문이 끝나는 순간은 대기 트럭이 없을 때가 아니라 모든 트럭이 다리를 지났을 때이다.
'''