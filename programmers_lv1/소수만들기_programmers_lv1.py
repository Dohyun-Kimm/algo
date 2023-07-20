def solution(nums):
    answer = -1
    nums_length = len(nums)
    checked = [0 for _ in range(len(nums))]
    partialSum = []
    cnt = 0

    # combination
    def combi(cur, start, length, arr):
        if cur == length:
            case = sum(arr)
            partialSum.append(case)
            return 0
        else:
            for i in range(start, nums_length):
                if checked[i] == 0:
                    checked[i] = 1
                    combi(cur + 1, i, length, arr + [nums[i]])
                    checked[i] = 0

    primes = [2, 3]
    for i in range(4, 998 + 999 + 1000):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    # print(primes)

    combi(0, 0, 3, [])
    for p in partialSum:
        if p in primes:
            cnt += 1

    return cnt

