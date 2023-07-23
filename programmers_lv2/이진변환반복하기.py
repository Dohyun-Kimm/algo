def solution(s):
    cnt, zeros = 0, 0

    while True:
        # print(s)
        ones = s.count('1')
        zeros += len(s) - ones
        if int(ones) == 1:
            cnt += 1
            break
        s = str(bin(int(ones)))[2:]
        cnt += 1
    return [cnt, zeros]


# self feedback
# int -> binary : bin()
# bin(int(ones)) = '0b'011010101
