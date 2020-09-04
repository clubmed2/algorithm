def solution(prices):
    answer = [i for i in range(len(prices)-1,-1,-1)]

    for i in range(len(prices)):
        for j in range(index+1,len(prices)):
            if( prices[j] < prices[i] ):
                answer[index] = j - index
                break
            else: answer[index] = j - index
    return answer

#새로 배운 점
'''
1. 슬라이싱은 시간을 꽤 잡아먹는다.
2. enumerate도 시간을 꽤 잡아먹는다.
3. collection.deque는 stack 또는 queue 처럼 사용할 수 있다.
'''