import re
def solution(dartscore):
    dart = re.findall('(\d+)([SDT])([*#]*)',dartscore)

    beforescore = 0
    score = []
    for index, i in enumerate(dart):
        tempScore = 0
        if( i[1] == 'S' ): tempScore += int(i[0])**1
        elif( i[1] == 'D' ): tempScore += int(i[0])**2
        elif( i[1] == 'T' ): tempScore += int(i[0])**3

        if( i[-1] == '*' ):
            if( index > 0 ): score[index-1] *= 2
            tempScore *= 2
        elif( i[-1] == '#' ):
            tempScore *= -1

        score.append(tempScore)
        
    return sum(score)

print(solution("1S*2T*3S"))

#새로 배운 점
'''
1. 정규식조건에 ()로 감싸면 각 조건에 맞게 분리되어 리스트로 반환된다. ex) 1S* > ['1','S','*']
'''