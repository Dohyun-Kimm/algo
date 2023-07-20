def solution(n):
    arr = []
    while n > 2:
        arr.append(n % 3)
        n = int(n / 3)
    arr.append(n)
    l = len(arr)
    ans = 0
    p = 0

    for i in range(l - 1, -1, -1):
        ans += arr[i] * (3 ** p)
        p += 1
        print(ans)
    return ans
