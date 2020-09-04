def distance(numpad, targetY, targetX, currentY, currentX):            
    #distArr[currentX][currentY]와 distArr[targetX][targetY]의 최단거리를 리턴한다.
    return abs(targetY - currentY) + abs(targetX - currentX)

def getYX(numpad, target):
    for i in range(4):
        for j in range(3):
            if( numpad[i][j] == target ):
                return i, j
    
def solution(numbers, hand):
    answer = ''
    numpad = [[1,2,3],
             [4,5,6],
             [7,8,9],
            ['*',0,'#']]
    LcurrentY, LcurrentX = 3, 0
    RcurrentY, RcurrentX = 3, 2

    for i in numbers:
        targetY, targetX = getYX(numpad, i)
        if( i == 1 or i == 4 or i == 7 ):
            answer += "L"
            LcurrentY, LcurrentX = targetY, targetX
        elif( i == 3 or i == 6 or i == 9 ):
            answer += "R"
            RcurrentY, RcurrentX = targetY, targetX
        else:
            if( distance(numpad, targetY, targetX, LcurrentY, LcurrentX) == distance(numpad, targetY, targetX, RcurrentY, RcurrentX) ):
                if( hand == "left" ):
                    answer += "L"
                    LcurrentY, LcurrentX = targetY, targetX
                else:
                    answer += "R"
                    RcurrentY, RcurrentX = targetY, targetX
            elif( distance(numpad, targetY, targetX, LcurrentY, LcurrentX) > distance(numpad, targetY, targetX, RcurrentY, RcurrentX) ):
                answer += "R"
                RcurrentY, RcurrentX = targetY, targetX
            else:
                answer += "L"
                LcurrentY, LcurrentX = targetY, targetX
            
    return answer

#새로 배운 점
'''
1. 이차원 배열의 거리는 y 좌표 차이 + x 좌표 차이로 구할 수 있다.
'''                
