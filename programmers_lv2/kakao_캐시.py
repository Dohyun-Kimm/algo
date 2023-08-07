from collections import deque

def solution(cacheSize, cities):
    answer = 0
    queue = deque()

    for city in cities:
        city = city.lower()
        if city not in queue:
            answer += 5                     # cache miss
            if cacheSize > 0:
                if len(queue) == cacheSize:
                    queue.popleft()
                queue.append(city)

        else:
            answer += 1                     # cache hit
            if queue:
                queue.remove(city)          # LRU update
                queue.append(city)
    return answer


#  문ㄴ제 풀이
# LRU를 구현하는 방법을 오래 생각했던것 같다.
# 가장 오래 사용되지 않은 캐시를 deque의 맨앞에 오도록 만들었고
# cache miss가 발생할때마다 popleft() 한뒤 append 해서 deque의 사이즈가 cachSize를 유지하게 했다.
# maxlen을 사용하면 popleft한뒤 append를 안해도 되는것 같다.
# cache hit이 발생하면, 해당 city는 deque 맨뒤로 가야했기때문에 deque에서 제거해주고 새로 append했다.

# 다른 사람 풀이
# def solution(cacheSize, cities):
#     import collections
#     cache = collections.deque(maxlen=cacheSize)
#     time = 0
#     for i in cities:
#         s = i.lower()
#         if s in cache:
#             cache.remove(s)
#             cache.append(s)
#             time += 1
#         else:
#             cache.append(s)
#             time += 5
#     return time