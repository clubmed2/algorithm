def solution(arr):
    answer = [arr[0]]
    
    #중복을 제거한 배열의 마지막이 현재 비교하려는 숫자와 다르면 추가한다.
    for i in arr:
        if not( answer[-1] == i ):
            answer.append(i)        

    return answer

#새로 배운 점
'''
1. 원래는 current변수를 만들고 current변수가 다른 숫자를 만날 때 추가했지만 위 방법으로 하면 current의 역할을 answer[-1]이 하므로 변수를 더 두지 않아도 된다.
'''            