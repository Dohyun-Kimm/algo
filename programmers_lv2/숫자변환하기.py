# dfs 시간 초과 발생
# dfs로 안될때는 bfs 생각해보기, 상황에 따라 DP 떠올리기

 #dfs code
# def solution(x, y, n):
#     answer = 1000000
#     # 계산으로 도달 한적이 있는지 확인하기 (중복 제거)
#     log = []
#
#     def search(start, target, addNum, cnt):
#         nonlocal answer
#         if start == target:
#             answer = min(answer, cnt)
#             return
#         elif start > target:
#             return
#         else:
#             a, b, c = start + addNum, start * 2, start * 3
#             search(a, target, addNum, cnt + 1)
#             search(b, target, addNum, cnt + 1)
#             search(c, target, addNum, cnt + 1)
#
#     search(x, y, n, 0)
#     if answer == 1000000:
#         return -1
#     else:
#         return answer
#




    # deque 활용한 bfs 풀이
from collections import deque
def solution(x, y, n):
    answer = -1
    log = deque()  # 변환할 숫자, 계산 수
    log.append((x, 0))
    visited = set()

    while log:
        a, cnt = log.popleft()
        if a == y:
            answer = cnt
            break
        else:
            if a + n <= y and a + n not in visited:
                visited.add(a + n)
                log.append((a + n, cnt + 1))
            if a * 2 <= y and a * 2 not in visited:
                visited.add(a * 2)
                log.append((a * 2, cnt + 1))
            if a * 3 <= y and a * 3 not in visited:
                visited.add(a * 3)
                log.append((a * 3, cnt + 1))

    return answer
