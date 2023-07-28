def solution(n, a, b):
    nums = '{0:b}'.format(n)
    rounds = 1

    # print(7//2)
    # 4->2->1, 7->4->2
    if abs(a - b) == 1 and a // 2 != b // 2:
        return rounds
    else:
        while rounds <= len(nums):
            rounds += 1
            a = a // 2 + 1 if a % 2 == 1 else a // 2
            b = b // 2 + 1 if b % 2 == 1 else b // 2
            # print(a,b)
            if abs(a - b) == 1 and a // 2 != b // 2:
                return rounds

    # return 0