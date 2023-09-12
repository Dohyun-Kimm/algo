# def solution(arr):
#     answer = [0,0]
#
#     def bfs(r, c, row, col):
#         print(r,c,row,col, '???')
#         bit = arr[r][c]
#
#         for i in range(r,row):
#             for j in range(c,col):
#                 if arr[r][c] != arr[i][j]:
#                     new_row, new_col = row // 2, col // 2
#                     print(r,c,new_row, new_col,new_row - r == 1 and new_col - c == 1)
#                     if new_row - r == 1 and new_col - c == 1:
#                         answer[bit] += 1
#                         return
#                     else:
#                         # print(r,c,new_row, new_col)
#                         bfs(r, c, new_row , new_col )
#                         bfs(r+new_row, c, row, new_col)
#                         bfs(r, c+new_col, new_row, col)
#                         bfs(r+new_row,c+ new_col, row, col)
#         answer[bit] += 1
#         return
#
#     bfs(0, 0, len(arr), len(arr[0]))
#
#     return answer
def solution(arr):
    answer = [0,0]
    def search(r,c,l):
        start = arr[r][c]
        for i in range(r,r+l):
            for j in range(c,c+l):
                if arr[i][j] != start:
                    l = l//2
                    search(r, c, l)
                    search(r+l, c, l)
                    search(r, c+l, l)
                    search(r+l, c+l, l)
                    return
        answer[start] += 1
    search(0,0, len(arr))

    return answer

solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
'''
[1,1,0,0]
[1,0,0,0]
[1,0,0,1]
[1,1,1,1]

'''
'''
배열의 [0,0] 에서 bfs 시작
i) bfs 돌면서 시작 점과 다른 숫자가 나온다면 행과 열을 반으로 나눈 값을 인자로 넣어 bfs 재귀
   새로운 시작점은 
    def bfs(행, 열, 시작점):
        for i in 행
             for j in 열
                 if 쪼갠 배열[i][j] != 시작점:
                    bfs(행//2, 열//2, 시작점 [0,0])
                    bfs(행//2, 열//2, 시작점 [0,0])
                    bfs(행//2, 열//2, 시작점 [0,0])
                    bfs(행//2, 열//2, 시작점 [0,0])
ii) 만약 범위 내의 모든 수가 같을때 1 혹은 0 자리에 추가하기.

'''

''' 
방법은 맞는데 풀이가 너무 지저분해진다.... 왜이럴까아아아아아아아아아ㅐ아아아아 
쉬운 방법으로 구현할 수 있는데 자꾸 어렵게 간다....
'''