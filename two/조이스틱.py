def upORdown(target):
    a = ord(target)-ord('A')
    b = 26-a
    return a if b > a else b
    
def solution(name):
    count = 0
    cur_i = 0
    name=list(name)
    while( True ):
        if( name[cur_i] != 'A' ):
            count += upORdown(name[cur_i])
            name[cur_i] = 'A'
            print(name)

        if( name == len(name)*['A'] ):
            break

        #A가 아닌 문자와 더 가까운 쪽으로 방향을 움직인다.
        for i in range(len(name)):
            if( name[cur_i+i] != 'A' ):
                break

        for j in range(len(name)):
            if( name[cur_i-j] != 'A' ):
                break

        if i > j:
            cur_i -= j
            count += j
        else:
            cur_i += i
            count += i

    return count

# 통과가 됐지만 맞는 풀이가 아님.
# 최소값(방향)을 선택하는 기준이 어려움

# print(solution("BBBAAAB")) #8
# print(solution("ABABAAAAABA")) #10
# print(solution("ABAAAAAAABA"))#: 6
# print(solution("AAB"))#: 2
# print(solution("AABAAAAAAABBB"))#: 12
# print(solution("ZZZ"))#: 5
# print(solution("BBBBAAABA"))#: 12
# print(solution("BBBBAAAAAB"))#: 10