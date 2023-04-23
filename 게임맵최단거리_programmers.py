<<<<<<< Updated upstream
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
=======
# 게임맵 최단 거리 고득점 키트

# test case
# [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
from collections import deque
answer = 0

def bfs(start, map):
    global answer
    d_row = [0,1,0,-1]
    d_col = [1,0,-1,0]
    queue = deque([start])
    map[start[0]][start[1]] = 1

    while queue:
        # for k in range(5):
        #     print(map[k])
        # print('==========')
        v = queue.popleft()
        # print('v:', v)

        for i in range(4):  # delta search
            # print('d_row : ', d_row[i], 'd_col: ', d_col[i])
            vr = v[0] + d_row[i]
            vc = v[1] + d_col[i]
            # print('vc vr:', vc, vr)
            if 0 <= vr < len(map) and 0 <= vc < len(map[0]) and map[vr][vc] == 1:
                map[vr][vc] = map[v[0]][v[1]] + 1 # 방문 표시
                queue.append([vr,vc])
    if map[-1][-1] != 1:
        answer = map[-1][-1]
    else:
        answer = -1
    return  answer


def solution(maps):
    global answer
    answer = 0
    bfs([0,0], maps)
    return answer




# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])
>>>>>>> Stashed changes
