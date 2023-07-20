def solution(sizes):
    row = 0
    col = 0
    for purse in sizes:
        r, c = max(purse), min(purse)
        if r > row:
            row = r
        if c > col:
            col = c

    return row * col