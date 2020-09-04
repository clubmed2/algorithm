import math

def solution(n):
    sqrt = n**(1/2)

    #if( sqrt.is_integer() ):
    if( sqrt%1 == 0 ):
        answer = (sqrt+1)**2
    else: answer = -1
    
    return answer

#새로 배운 점
'''
1. float가 자연수인지 판별할 때 float.is_integer()대신 float%1==0
2. math.sqrt(n)대신 n**(1/2)
'''
