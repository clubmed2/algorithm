def solution(n, a, b):
    people = [i+1 for i in range(n)]
    temp = n
    jisu = 0

    while(temp != 0):
        temp = temp >> 1
        jisu += 1
    for i in range(jisu):
        for j in range(n):
            people[j] = (people[j]+1) // 2
        if(people[a-1] == people[b-1]):
            return i+1


# 새로 배운 점
'''
1. 비트연산은 결과를 리턴함.
'''
