import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while(True):
        first = heapq.heappop(scoville)
        if(first >= K):
            return count
        if(len(scoville) == 0):
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + (second * 2))
        count += 1


'''
새로 배운 점
1. heapq
'''
