import re
from itertools import permutations


def solution(expression):
    answer = 0
    chars = ['+', '-', '*']
    chars = list(permutations(chars))

    for i in chars:
        extemp = re.split('([+*-])', expression)
        for j in i:
            find = 1
            while(find < len(extemp)):
                if(extemp[find] == j):
                    if(j == '+'):
                        temp = str(
                            int(extemp[find-1])+int(extemp[find+1]))
                        for p in range(3):
                            del extemp[find-1]
                        extemp.insert(find-1, temp)
                        find = 1
                    elif(j == '-'):
                        temp = str(
                            int(extemp[find-1])-int(extemp[find+1]))
                        for p in range(3):
                            del extemp[find-1]
                        extemp.insert(find-1, temp)
                        find = 1
                    elif(j == '*'):
                        temp = str(
                            int(extemp[find-1])*int(extemp[find+1]))
                        for p in range(3):
                            del extemp[find-1]
                        extemp.insert(find-1, temp)
                else:
                    find += 2
        if abs(int(extemp[0])) > answer:
            answer = abs(int(extemp[0]))
    return answer


# 새로 배운 점
'''
1. re.split()
'''
