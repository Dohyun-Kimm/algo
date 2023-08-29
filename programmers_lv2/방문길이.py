def solution(dirs):
    answer = 0
    command = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    logs = set()
    x, y = 0, 0
    for d in dirs:
        dx, dy = x + command[d][0], y + command[d][1]
        if -5 <= dx <= 5 and -5 <= dy <= 5:
            logs.add((x, y, dx, dy))
            logs.add((dx, dy, x, y))
            x, y = dx, dy
    # print(logs)

    return len(logs) // 2

# 문제풀이
# 처음 가보는길을 따지는것이 중요했던 문제다.
# set을 사용해서 중복되는 길을 제거 했다.
# 처음 가는 길을 양방향으로 저장했기 때문에
# 정답을 출력할때는 set의 길이를 2로 나누면 된다.