from itertools import cycle


def solution(answers):
    one = cycle([1, 2, 3, 4, 5])
    two = cycle([2, 1, 2, 3, 2, 4, 2, 5])
    three = cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    result_score = [0, 0, 0]
    result = []

    for i in range(len(answers)):
        if(answers[i] == next(one)):
            result_score[0] += 1
        if(answers[i] == next(two)):
            result_score[1] += 1
        if(answers[i] == next(three)):
            result_score[2] += 1
    for i, j in enumerate(result_score):
        if(j == max(result_score)):
            result.append(i+1)
    answer = result
    return answer


# 새로 배운 점
'''
1. itertools, cycle(), next()
'''
