def solution(m, n, board):
    deleteBlocks = [[0, 0]]
    count = 0

    for y in range(m):
        board[y] = list(board[y])
    while(deleteBlocks != []):
        deleteBlocks = []
        for y in range(m-1):
            for x in range(n-1):
                if(board[y][x] != "" and board[y][x] == board[y+1][x] == board[y][x+1] == board[y+1][x+1]):
                    deleteBlocks.append([y, x])
                    deleteBlocks.append([y+1, x])
                    deleteBlocks.append([y, x+1])
                    deleteBlocks.append([y+1, x+1])
        for y, x in deleteBlocks:
            if(board[y][x] != ""):
                board[y][x] = ""
                count += 1
        for x in range(n):
            for y in range(m-1, 0, -1):
                if(board[y][x] == ""):
                    temp = y
                    while(board[temp][x] == "" and temp >= 0):
                        temp -= 1
                    if(temp != -1):
                        board[y][x], board[temp][x] = board[temp][x], ""
    return count


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))  # 14
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC",
                      "TRRRAA", "TTMMMF", "TMMTTJ"]))  # 15
