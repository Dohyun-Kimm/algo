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
                        if 0 <= i + x < 19 and 0 <= j + y < 19 and board[i+x][j+y] == stone:
                            break
                        if 0<= i-dx[k] < 19 and 0<=j-dy[k]<19 and board[i-dx[k]][j-dy[k]] == stone:
                           break
                        else:
                            # print('-----')
                            print(stone)
                            print(i+1,j+1)
                            flag = False
                            break
                    elif board[i+x][j+y] != stone:
                        break
                    else:
                        z += 1
                        x = dx[k]*z
                        y = dy[k]* z
if flag == True:
    print(0)