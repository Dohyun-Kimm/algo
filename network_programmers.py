# 네트워크
# 2023 04 18
# 몇개의 네트워크가 있는지 카운트 하기.
# dfs가 막힐 때 마다 count 1
# 풀이: 모든 지점에서 dfs 시작하기
# 시작 지점이 방문한 곳이라면 스킵하기.
# dfs가 끝나는 지점에서 count 해주기.

visited = []
def dfs(v,graph):
    global visited
    visited[v] = 1
    for i in graph[v]:
        if not visited[i] and graph[i] ==1:
            dfs(i,graph)

def solution(n, computers):
    global visited
    answer = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        dfs(i,computers)
        answer += 1

    return answer

