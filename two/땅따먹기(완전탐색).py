answer = 0


def search(land, y, x, temp):
    global answer
    temp += land[y][x]

    if(y == len(land)-1):
        if(answer < temp):
            answer = temp
        return

    for i in range(len(land[0])):
        if(i != x):
            search(land, y+1, i, temp)


def solution(land):
    for i in range(len(land[0])):
        search(land, 0, i, 0)

    return answer


# 새로 배운 점
'''
1. 완전탐색이 더 느리다.
'''
