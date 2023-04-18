# dfs로 게임맵 풀기

# basic dfs code
def basic_dfs (v, visited,graph):
    visited[v] = True
    print(v,end='')
    for i in graph[v]:
        if not visited[i]:
            basic_dfs(i,visited, graph)

visited = []
answer = 0
def dfs(vr,vc,visit,graph):
    global answer
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visit[vr][vc] += 1
    for j in range(len(graph)):
        print(visit[j])
    print(('==='))

    for i in range(4):
        r = vr + dx[i]
        c = vc + dy[i]
        if 0 <= r < len(graph) and 0 <= c < len(graph[0]):
            if graph[r][c] != 0 and not visit[r][c]:         # 방문 하지 않았다면
                visit[r][c] = visit[vr][vc]
                dfs(r,c,visit,graph)
                visit[r][c] = 1
    if visit[-1][-1] == 0:
        answer = -1
    else :
        answer = visit[-1][-1]
    return answer

def solution(maps):
    global visited, answer
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    dfs(0,0,visited,maps)
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))