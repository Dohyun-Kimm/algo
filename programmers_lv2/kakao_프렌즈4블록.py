def solution(m, n, board):
    answer = 0
    board_arr = []
    for row in range(m):
        board_arr.append(list(map(str, board[row])))
    dm = [0, 1, 1]
    dn = [1, 0, 1]
    while True:
        checked = [[0 for _ in range(n)] for _ in range(m)]
        # 2x2 찾기
        for i in range(m):
            for j in range(n):
                check = 0
                for d in range(3):
                    x = i + dm[d]
                    y = j + dn[d]
                    if -1 < x < m and -1 < y < n:
                        if board_arr[x][y].isalpha() and board_arr[x][y] == board_arr[i][j]:
                            check += 1
                if check == 3:
                    checked[i][j] = 1
                    for d in range(3):
                        checked[i + dm[d]][j + dn[d]] = 1
        tmp = answer
        for k in range(m):
            for l in range(n):
                answer += checked[k][l]
                if checked[k][l]:
                    board_arr[k][l] = ''
        if tmp == answer:
            return answer

        for r in range(1, m):
            for c in range(n):
                if board_arr[r][c] == '':
                    for rr in range(r, 0, -1):
                        board_arr[rr][c], board_arr[rr - 1][c] = board_arr[rr - 1][c], board_arr[rr][c]

# 리뷰
# 풀이 과정을 처음 부터 끝까지 종이에 가능한 구체적으로 그려본뒤 코드를 적으려고 했다.
# 이 문제를 풀면서 느낀 것은, 내가 구상하는 과정에서 오류가 발생한다는 것이었다.
# 4블록을 제거하고 위에 있는 블록을 내리는 과정을 구현 할때 처음 생각한 것과 달라서 시간을 많이 허비 했다.
# 풀이의 처음 부터 끝까지 가능한 구체적으로 구상하고 코드를 적는 방법이 효과적이라는것을 어렴풋이 느낄 수 있었다.