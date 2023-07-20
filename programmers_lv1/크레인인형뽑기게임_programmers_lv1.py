def solution(board, moves):
    answer = 0
    # moves : 열 번호
    # 2차원행렬 90도 돌리기
    row_length = len(board)
    col_length = len(board[0])
    rotate_board = [[0] * row_length for _ in range(col_length)]
    for i in range(row_length):
        for j in range(col_length):
            rotate_board[j][i] = board[i][j]
    #     for k in range(col_length):
    #         print(rotate_board[k])

    stack = []
    for m in moves:
        for n in range(col_length):
            if rotate_board[m - 1][n] > 0:
                # print(rotate_board[m-1][n],m,n)
                stack.append(rotate_board[m - 1][n])
                rotate_board[m - 1][n] = 0
                break
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2
            # print(stack)

    return answer