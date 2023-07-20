def solution(n):
    answer = 0
    arr = [1 for i in range(n + 1)]

    for i in range(2, len(arr)):
        if arr[i]:
            j = 2
            while j * i < n + 1:
                arr[i * j] = 0
                j += 1
    # print(arr)
    for k in range(2, len(arr)):
        if arr[k]:
            answer += 1
    return answer