from collections import deque

visited = []
def bfs(graph,start,visited):
    queue = deque([start])
    visited[start[0]][start[1]] = 1

    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in range(graph[v]):
            if graph[v][i] not in visited:
                queue.append(i)
                visited[i] = 1


def solution(maps):
    global visited
    visited= [[0 for _ in range(len(maps))] for _ in range(len(maps))]
    answer = 0
    bfs(maps,[0,0],visited)
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))