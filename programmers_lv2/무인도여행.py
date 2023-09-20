from collections import deque


def solution(maps):
    answer = []
    checked = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # bfs 문제
    cnt = 0
    def bfs(row, col):
        nonlocal cnt
        queue = deque()
        queue.append([row,col])
        checked[row][col] = True
        while queue:
            tmp = queue.popleft()
            p, q = tmp[0], tmp[1]
            cnt += int(maps[p][q])
            # print('--------', p, q)
            for i in range(4):
                x = p + dx[i]
                y = q + dy[i]
                if 0 <= x < len(maps) and 0 <= y < len(maps[0]):
                    # print(maps[x][y],x,y)
                    if checked[x][y] == False and maps[x][y] != 'X':
                        checked[x][y] = True
                        queue.append([x, y])


    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] != 'X'and checked[r][c] == False:
                cnt = 0
                bfs(r, c)
                if cnt > 0:
                    answer.append(cnt)
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))