def solution(wallpaper):
    min_row, min_col, max_row, max_col = 50, 50, 0, 0
    for r in range(len(wallpaper)):
        for c in range(len(wallpaper[0])):
            if wallpaper[r][c] == '#':
                min_row = min(min_row, r)
                min_col = min(min_col, c)
                max_row = max(max_row, r + 1)
                max_col = max(max_col, c + 1)

    return [min_row, min_col, max_row, max_col]