def solution(n):
    # arr = [0 for _ in range(n+1)]
    arr = [0] * (n + 1)

    arr[1] = 1
    arr[2] = 2
    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    if n < 3:
        return n
    else:
        return arr[n] % 1234567
# 아래 코드와 차이점이 뭔지 모르겠음.  아 알았다 n=2일때 for문ㅇ ㅣ실행이 안된다..........
    # def solution(n):
    #     if n < 3:
    #         return n
    #     d = [0] * (n + 1)
    #     d[1] = 1
    #     d[2] = 2
    #     for i in range(3, n + 1):
    #         d[i] = d[i - 1] + d[i - 2]
    #     return d[n] % 1234567