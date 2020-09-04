def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


# 새로 배운 점
'''
1. str형으로 비교하면 맨 앞부터 비교하기 때문에 자릿수는 상관없다.
2. [0,0,0]일 때 0을 반환해야 하지만 000을 반환해서 오류가 났었는데 이 경우 int로 감싸면 된다.
'''
