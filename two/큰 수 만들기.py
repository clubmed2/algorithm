def solution(number, k):
    number = list(number)
    picked = []

    picked.append(number[0])
    for i in range(1, len(number)):
        # k를 다 소진하지 않고, 비교할 대상이 있고, 비교할 대상이 더 작다면
        while(k > 0 and picked and number[i] > picked[-1]):
            picked.pop()
            k -= 1
        # k를 다 소진했다면 남은 숫자들과 합친다.
        if(k == 0):
            picked += number[i:]
            return ''.join(picked)
        picked.append(number[i])
    return ''.join(picked[:-k])


# 새로 배운 점
'''
1. 슬라이싱과 max로 인해 시간초과가 났다. 가장 앞에서부터 돌면서 자신보다 작은 애가 뒤에 있다면 걔를 없애고 k를 하나 줄인다. 그러면 O(n)만큼 걸린다.
'''
