# 친구비
# 230435
# 가장 적은 비용으로 최대 친구 만들기

from collections import deque


def bfs(node, fee):
    global total_fee
    queue = deque()
    queue.append(node)
    visited[node] = 1
    while queue:
        a = queue.popleft()
        fee = min(friend_fee[a], fee)
        # print(a, fee)
        for n in graph[a]:
            if visited[n] == 0:
                visited[n] = 1
                # print(fee,n,'???')
                queue.append(n)

    if fee != 10000001:
        total_fee += fee


N, M, k = map(int, input().split())
table = [0]
total_fee = 0
friend_fee = list(map(int,input().split()))
friend_fee = table + friend_fee
# print(friend_fee)
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for i in range(M):
    v,w = map(int,input().split())
    graph[v].append(w)
    graph[w].append(v)

# bfs 돌면서 가장 작은 친구비 찾기.
for x in range(1,N+1):
    if not visited[x]:
        bfs(x, 10000001)

if total_fee<=k:
    print(total_fee)
else:
    print('Oh no')
