def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        #binary = (n-len(bin(i|j)[2:]))*'0'+str(bin(i|j)[2:])
        #binary = str(bin(i|j)[2:]).rjust(n,'0')
        binary = str(bin(i|j)[2:]).zfill(n)
        binary = binary.replace('1','#').replace('0',' ')
        answer.append(binary)
    
    return answer

#새로 배운 점
'''
1. rjust(10, '0')는 '0'으로 왼쪽을 빈 부분을 채움. ljust()는 오른쪽을 채움
2. str.zfill(50)은 0으로 왼쪽을 빈 부분을 채움
'''  