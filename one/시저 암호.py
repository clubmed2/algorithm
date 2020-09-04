def solution(s, n):
    new = ""

    for i, j in enumerate(s):
        if( j == ' ' ):
            new += ' '
        else:
            if( j.islower() ):
                #ord(j) - ord('a')를 하는 이유는 j의 순수한 알파벳 인덱스를 구하기 위해서다.
                #그 다음 n만큼 밀어주되, 순환이 되도록 26을 나눠준다.
                new += chr(ord('a') + ((ord(j) - ord('a') + n) % 26))
            else:
                new += chr(ord('A') + ((ord(j) - ord('A') + n) % 26))
    answer = new
    return answer

#새로 배운 점
'''
1. ord(), chr()
2. 순환 사고
'''