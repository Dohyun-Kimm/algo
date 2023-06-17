def solution(d, budget):
    d.sort()
    idx = 0
    answer = 0
    while idx < len(d):
        budget -= d[idx]
        idx += 1
        if budget >= 0:
            answer += 1
    return answer