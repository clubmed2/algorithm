import collections


def solution(cacheSize, cities):
    cache = collections.deque(maxlen=cacheSize)
    cachehit = 0
    cachemiss = 0

    if(cacheSize == 0):
        return 5*len(cities)
    for i in cities:
        i = i.lower()
        if(i in cache):
            cachehit += 1
            cache.remove(i)
            cache.append(i)
        else:
            cachemiss += 1
            cache.append(i)
    return cachehit*1+cachemiss*5


# 새로 배운 점
'''
1. collections.deque에서 maxlen을 설정하면 자동으로 pop(0)된다.
'''
