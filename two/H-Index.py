def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations)):
        print(citations[i])
        # 3(번 인덱스)보다 citations[3]이 크다는 것은 4개의 논문이 3번 이상 인용되었다는 뜻이다. (정렬되었기 때문에) -> 계속 검사한다.
        # 3(번 인덱스)보다 citations[3]가 작다는 것은 앞선 3개의 논문이 3번 이상 인용되었고, 나머지는 3번 이하로 인용되었다.
        # 따라서 i번 째 인덱스가 citations[i]보다 작은 순간, i가 H-index의 최대값이다.
        if(citations[i] < i):
            return i
    return len(citations)


# 새로 배운 점
'''
1. 정렬 사용 여부
'''
