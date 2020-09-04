def solution(n, m):
#최대공약수
    #유클리드 호제법
    i, j = max(n, m), min(n, m)
    while( i%j != 0 ):
         i, j = j, i % j
    yak = j
    #반복문
    # for i in range(1, m+1 if n > m else n+1):
    #     if( n%i == 0 and m%i == 0 ):
    #         max = i

#최소공배수
    #최대공약수 이용
    bae = int(n*m / yak)

    #반복문 
    # for i in range(n*m, n-1 if n > m else m-1, -1):
    #     if( i%n==0 and i%m==0 ):
    #         min = i
            
    answer = [yak, bae]
    return answer

#새로 배운 점
'''
1. 최대공약수는 1부터 둘 중 작은 수까지 나눈다.
2. 최소공배수는 두 수의 곱부터 더 큰 수까지 나눠서 찾는다.
3. 반복문 1씩 증가할 땐 +1이지만 1씩 감소할 땐 -1까지 찾는다.
4. 최소공배수는 두 수의 곱를 최소공약수로 나눈 값이다.
'''                