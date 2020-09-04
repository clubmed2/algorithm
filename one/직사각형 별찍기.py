a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print("*",end='')
    if( i != b-1 ): print()

#새로 배운 점
'''
1. 개행 횟수는 별 출력 줄 -1이다.
'''  