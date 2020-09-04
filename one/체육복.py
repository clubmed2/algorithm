def solution(n, lost, reserve):
    got = []
    canGive = []
    answer = 0
    
    for i in range(n):
        #잃어버렸는데
        if( i+1 in lost ):
            #여분이 있다면
            if( i+1 in reserve ):
                got.append(1)
                canGive.append(0)
            #여분이 없다면
            else:
                got.append(0)
                canGive.append(0)
        #잃어버리지 않았는데
        else:
            #여분이 있다면
            if( i+1 in reserve ):
                got.append(1)
                canGive.append(1)
            #여분이 없다면
            else:
                got.append(1)
                canGive.append(0)

    for i in lost:
        #내가 가지지 못했고 뒷 사람이 빌려 줄 수 있다면 빌린다.
        if( i != 1 and got[i-1] == 0 and canGive[i-2] == 1 ):
            got[i-1] += 1
            canGive[i-2] -= 1
        #내가 가지지 못했고 앞 사람이 빌려 줄 수 있다면 빌린다.
        elif( i != n and got[i-1] == 0 and canGive[i] == 1 ):
            got[i-1] += 1
            canGive[i] -= 1          

    for i in got:
        if( i==1 ):
            answer += 1
            
    return answer

#새로 배운 점
'''
1. 잃어버려서 여분으로 대체했지만 마지막에 lost반복문에서 여분으로 대체한 경우를 예외처리 하지 않았었다. 여분이 있는 경우 lost 및 reserve배열에서 제외하려 했으나 반복문 중 제외를 하면 누락되는 경우가 발생했기 때문에 마지막에 여분을 빌릴 때 '내가 가지고 있지 않는 경우라는 조건'을 추가하였다.
'''
