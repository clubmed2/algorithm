import collections


def solution(nums):
    return int(min(len(nums)/2, len(set(nums))))


# 새로 배운 점
'''
1. 카운트가 필요없고 단순히 중복제거를 위한거라면 set()을 사용하자
2. 짝수를 2로 나눈 결과는 몫과 같다
'''
