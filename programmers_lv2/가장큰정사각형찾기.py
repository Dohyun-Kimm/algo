def solution(board):
    # answer = 1234
    # board와 똑같은배열을 만들고 가장큰사각형의 크기를 누적하는 방식으로.
    # 현재보고있는 좌표가 1 일때
    # 현재 좌표의 좌, 상, 좌상 좌표의 최소 값 + 1

    check_board = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for i in range(len(board)):
        for j in range(len(board[0])):
            check_board[i + 1][j + 1] = board[i][j]

    for i in range(1, len(check_board)):
        for j in range(1, len(check_board[0])):
            if check_board[i][j] == 1:
                check_board[i][j] = min(check_board[i - 1][j], check_board[i][j - 1], check_board[i - 1][j - 1]) + 1
    # print(check_board)

    answer = 0
    for a in range(len(check_board)):
        for b in range(len(check_board[0])):
            answer = max(check_board[a][b], answer)
    return answer ** 2