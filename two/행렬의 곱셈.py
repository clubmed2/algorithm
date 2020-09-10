def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        temp2 = []
        for j in range(len(arr2[0])):
            temp = []
            for k in range(len(arr1[0])):
                temp.append(arr1[i][k]*arr2[k][j])
            temp2.append(sum(temp))
        answer.append(temp2)
    return answer


# 새로 배운 점
'''
1. 2차원 배열을 선언할 때 [[0]*3]*3말고, [[0 for i in range(3)] for j in range(3)]하자
'''
