def solution(n, m, section):
    answer = 0
    wall = [-1] + [1] * n
    for sec in section:
        wall[sec] = 0

    for i in range(1, n + 1):
        if wall[i] == 0:
            answer += 1
            wall[i: i + m] = [1] * m

    return answer