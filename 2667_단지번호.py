# 230423
# 단지번호 붙이기
# 델타 탐색 + bfs
# bfs 시작 횟수 카운트 하기.


from collections import deque

def bfs(u,v,c):
    global answer,N
    queue = deque()
    queue.append([u,v])
    c += 1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    # print('====')
    while queue:
        new = queue.popleft()
        x,y = new[0],new[1]
        visited[x][y] = answer

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(nx,ny)
            if -1< nx < N and -1< ny < N:
                # print('range', nx, ny)
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    # print('check')
                    queue.append([nx,ny])
                    visited[nx][ny] = answer
                    c += 1
                    # print(c,nx,ny)
    num.append(c)


N = int(input())
answer = 0
num = []
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))

visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j]:
            answer+=1
            count = 0
            bfs(i,j,count)


print(answer)
num = sorted(num)
for i in range(len(num)):
    print(num[i])