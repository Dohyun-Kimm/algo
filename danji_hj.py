# boj_2667_단지번호붙이기

N = int(input())
danji = []
visited = [[0] * N for _ in range(N)]

for _ in range(N):
    danji.append(list(map(int, input())))

ni = [0, 1, 0, -1]
nj = [1, 0, -1, 0]

houses = []
cnt = 0
def dfs(cur_i, cur_j):
    global cnt
    visited[cur_i][cur_j] = 1
    cnt += 1

    for i in range(4):
        cur_i = cur_i + ni[i]
        cur_j = cur_j + nj[i]
        if 0 <= cur_i < N and 0 <= cur_j < N and danji[cur_i][cur_j] and visited[cur_i][cur_j] == 0:
            print(cur_i, cur_j)
            dfs(cur_i, cur_j)

ans = 0
for i in range(N):
    for j in range(N):
        if danji[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            houses.append(cnt)
            cnt = 0


print(ans,houses)