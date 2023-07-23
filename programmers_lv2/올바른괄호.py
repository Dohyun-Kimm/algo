def solution(s):
    answer = True
    opened = []
    for t in s:
        if t == '(':
            opened.append(t)
        else:
            if opened:
                opened.pop()
            else:
                return False

    if opened:
        return False
    else:
        return True

    # return len(st) == 0