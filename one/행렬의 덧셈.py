def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        #answer.append([arr1[i][k] + arr2[i][k] for k in range(len(arr1[i]))])
        answer.append([x+y for x, y in zip(arr1[i], arr2[i])])
    return answer


# 새로 배운 점
'''
1. 리스트 인덱스끼리 덧셈방법
2. zip
'''
