from collections import deque

def bfs(start, end,maps):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    queue = deque()
    flag  = False
    # print(start)
    # 초기값
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == start:
                queue.append([i,j,0])
                visited[i][j] = True
                flag = True
                break
        if flag:
            break

    while queue:
        r,c,time = queue.popleft()
        if maps[r][c] == end:
            return time
        for i in range(4):
            x = r + dx[i]
            y = c + dy[i]
            if 0<=x <len(maps) and 0<= y <len(maps[0]) and maps[x][y] != 'X':
                if visited[x][y] == False:
                    queue.append([x,y,time+1])
                    visited[x][y] = True
    return -1

def solution(maps):
    # S -> L, L-> E 두가지 경우 계산하기
    # 두 경로 중 하나라도 길이 존재 하지 않으면 return  -1
    path1 = bfs("S","L",maps)
    path2 = bfs("L","E",maps)
    # print(path1, path2)
    if path1 == -1 or path2 == -1:
        return -1
    else:
        return path2 + path1


print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))