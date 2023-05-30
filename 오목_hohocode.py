# 오목 승패를 판단하는 알고리즘
# dfs...?
# 1 또는 2가 나오면 3방 델타 탐색 우 우하 하.
# 오목이 되는 경우  5번 연속 같은 방향으로 같은 숫자 나올때
# 아닌경우 : 5번 되기 전에 다른 숫자가 나오는 경우

board = [list(map(int,input().split())) for _ in range(19)]

start_point = [0,0]
stone = 0
dx = [0,1,1,-1]
dy = [1,1,0,1]
flag = True

for j in range(19):
    if flag == False:
        break
    for i in range(19):
        if flag == False:
            break
        # 돌이 있을때
        if board[i][j] > 0:
            stone = board[i][j]
            # print(i,j)
            # stone_x = i ,stone_y = j
            # delta search
            for k in range(4):
                z = 1
                x = dx[k] *z
                y = dy[k] *z
                # print(stone,'--------',i,j,'flag',flag,'x,y',i+x,j+y)
                while flag and 0<=i+x < 19 and 0<=j+y <19 :
                    # print(board[i+x][j+y])
                    # 5목일 때
                    if z ==4 and board[i+x][j+y] == stone:
                        # 6목 확인
                        z += 1
                        x = dx[k] * z
                        y = dy[k] * z
                        # print(i+x,j+y, 'z',z)
                        if 0 <= i + x < 19 and 0 <= j + y < 19 and 0<= i-dx[k] < 19 and 0<=j-dy[k]<19:
                            if board[i+x][j+y] != stone and board[i-dx[k]][j-dy[k]]!=stone:
                                # print('?')
                                # 그전 돌이 같은 색이 아닌지 확인
                                print(stone)
                                print(i + 1, j + 1)
                                flag = False
                            else:
                                # print('???')
                                break
                        else:
                            # print('-----')
                            print(stone)
                            print(i+1,j+1)
                            flag = False
                    elif board[i+x][j+y] != stone:
                        break
                    else:
                        z += 1
                        x = dx[k]*z
                        y = dy[k]* z
if flag == True:
    print(0)
