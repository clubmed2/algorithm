import collections


def solution(people, limit):
    boat = 0
    people = collections.deque(sorted(people))

    while(people):
        boat += 1
        boatweight = limit
        if(len(people) > 1 and people[0]+people[-1] <= boatweight):
            people.popleft()
            people.pop()
        else:
            people.pop()
    return boat


# 새로 배운 점
'''
1. 무거운 사람부터 태워야 효율적으로 태울 수 있다.
2. pop()은 O(1)이지만 pop(0)은 O(n)이다.
    2.1 collections.deque()를 사용하여 popleft()를 해주면 O(1)로 구현할 수 있다.
'''
