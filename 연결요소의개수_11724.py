# N,M
#
def dfs(z, maps):
    global visited
    visited[z] += 1
    for a in maps[z]:
        if not visited[a]:
            dfs(a, maps)



N,M = map(int,input().split())
graph = [[] for _ in range(N+1)] # 0 생략하고 1인덱스 부터
visited = [0 for _ in range(N+1)]
answer = 0

for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for j in range(1, N+1):
    if not visited[j]:
        dfs(j, graph)
        # print(visited)
        answer += 1
# print(graph)

print(answer)
