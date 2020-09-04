def solution(board, moves):
    picked = []
    score = 0

    for i in moves:
        i -= 1
        for j in range(len(board)):
            if(board[j][i] != 0):
                picked.append(board[j][i])
                board[j][i] = 0

                # 연속된 인형 찾기
                if(len(picked) >= 2 and picked[-1] == picked[-2]):
                    score += 2
                    picked.pop()
                    picked.pop()
                break
    answer = score
    return answer


# 새로 배운 점
'''
1. list.pop()은 가장 마지막 값을 리턴하고 list에서 제외한다.
'''
