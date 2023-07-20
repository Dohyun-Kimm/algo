def solution(lottos, win_nums):
    answer = []
    cnt = 0
    err_num = lottos.count(0)
    for num in lottos:
        if num in win_nums:
            cnt += 1
    if cnt < 2:
        min_prize = 6
    else:
        min_prize = 7 - (cnt)
    if cnt + err_num < 2:
        max_prize = 6
        min_prize = 6
    else:
        max_prize = 7 - (cnt + err_num)

    return [max_prize, min_prize]