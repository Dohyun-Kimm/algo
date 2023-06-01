def solution(array):
    mode = [0]*1000
    for i in array:
        mode[i] +=1
    max_cnt = max(mode)
    cnt_mode= 0
    for i in mode:
        if i == max_cnt:
            cnt_mode +=1
    if cnt_mode > 1:
        answer = -1
    else:
        answer = mode.index(max_cnt)
    return answer


##   array.count

# def solution(array):
#     answer = 0
#     idx = [0] * 1001
#     for i in array:
#         idx[i] +=1
#     if idx.count(max(idx)) >1:
#         return -1
#     return idx.index(max(idx))