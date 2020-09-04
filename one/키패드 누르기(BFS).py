def distance(numpad, targetY, targetX, currentY, currentX):            
    #distArr[currentX][currentY]와 distArr[targetX][targetY]의 최단거리를 리턴한다.
    distArr = [[0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0]]
    visited = [[0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0]]
    vectors = [[1,0],
               [0,-1],
               [-1,0],
               [0,1]]

    queue = [[currentY, currentX]]
    visited[currentY][currentX] = 1

    while( queue != [] ):
        currentY, currentX = queue.pop(0)
        for i in range(4):
            if( currentY+vectors[i][0] >= 0 and currentY+vectors[i][0] <= 3 and currentX+vectors[i][1] >= 0 and currentX+vectors[i][1] <= 2 ):
                if( visited[currentY+vectors[i][0]][currentX+vectors[i][1]] == 0 ):
                    before = distArr[currentY][currentX]
                    visited[currentY+vectors[i][0]][currentX+vectors[i][1]] = 1
                    distArr[currentY+vectors[i][0]][currentX+vectors[i][1]] += (before + 1)
                    if( currentY+vectors[i][0] == targetY and currentX+vectors[i][1] == targetX ):
                        return distArr[targetY][targetX]
                    queue.append([currentY+vectors[i][0], currentX+vectors[i][1]])

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
    LcurrentY, RcurrentX = 3, 0
    RcurrentY, RcurrentX = 3, 2

    for i in numbers:
        if( i == 1 or i == 4 or i == 7 ):
            answer += "L"
            LcurrentY, LcurrentX = getYX(numpad, i)
        elif( i == 3 or i == 6 or i == 9 ):
            answer += "R"
            RcurrentY, RcurrentX = getYX(numpad, i)
        else:
            targetY, targetX = getYX(numpad, i)
            if( distance(numpad, targetY, targetX, LcurrentY, LcurrentX) == distance(numpad, targetY, targetX, RcurrentY, RcurrentX) ):
                if( hand == "left" ):
                    answer += "L"
                    LcurrentY, LcurrentX = getYX(numpad, i)
                else:
                    answer += "R"
                    RcurrentY, RcurrentX = getYX(numpad, i)
            elif( distance(numpad, targetY, targetX, LcurrentY, LcurrentX) > distance(numpad, targetY, targetX, RcurrentY, RcurrentX) ):
                answer += "R"
                RcurrentY, RcurrentX = getYX(numpad, i)
            else:
                answer += "L"
                LcurrentY, LcurrentX = getYX(numpad, i)
            
    return answer
#print(solution( [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))

#새로 배운 점
'''
1. BFS가 더 느리다.
'''                
