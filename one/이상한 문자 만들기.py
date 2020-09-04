def solution(s):
    answer = s.split(' ')
    new = [''] * len(answer)

    for a, i in enumerate(answer):
        for b, j in enumerate(i):
            if(b % 2 == 0):
                new[a] += j.upper()
            else:
                new[a] += j.lower()
    answer = ' '.join(new)
    return answer


# 새로 배운 점
'''
1. 각 단어는 하나 이상의 공백문자로 구분되어 있다. split()을 하게 되면 마지막에 결과를 출력할 때 ' '.join()에서 하나 이상의 공백들이 하나의 공백으로만 구분되게된다. 따라서 split(' ')으로 모든 공백을 각각 나누고 마지막에 ' '.join()함으로써 나눈 공백들을 다시 복원한다.
'''
