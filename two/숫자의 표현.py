def solution(n):
    count = 0

    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if(sum >= n):
                if(sum == n):
                    count += 1
                    break
                else:
                    break
    return count


# 새로 배운 점
'''
1. 없음
'''
