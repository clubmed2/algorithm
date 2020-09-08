numbers = []
target = 0


def dfs(depth, current, answer):
    if depth == len(numbers):
        answer.append(current)
        return
    dfs(depth+1, current+numbers[depth], answer)
    dfs(depth+1, current-numbers[depth], answer)


def solution(inumbers, itarget):
    global numbers
    numbers = inumbers
    global target
    target = itarget
    answer = []

    dfs(0, 0, answer)
    return answer.count(target)


# 새로 배운 점
'''
1. 전역 변수를 global로 선언하지 않으면 함수 안에서 수정할 수 없다.
2. list, dict, set은 call by reference로 넘어간다.
'''
