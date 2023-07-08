def solution(n, lost, reserve):
    answer = 0
    a_lost = list(set(lost) - set(reserve))
    a_reserve = list(set(reserve) - set(lost))
    for r in a_reserve:
        front = r - 1
        back = r + 1
        if front in a_lost:
            a_lost.remove(front)
        elif back in a_lost:
            a_lost.remove(back)

    return n - len(a_lost)