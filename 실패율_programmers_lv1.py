def solution(N, stages):
    answer = []
    arr = [0] * (N + 2)
    for idx, stage in enumerate(stages):
        arr[stage] += 1
        # print(arr)
    failure = dict()
    users = 0
    for i in range(1, len(arr) - 1):
        print(arr[i], (len(stages) - users))
        if (len(stages) - users) != 0:
            failure[i] = (arr[i] / (len(stages) - users))
            users += arr[i]
        else:
            failure[i] = 0
    ans = sorted(failure.items(), key=lambda x: x[1], reverse=True)
    for a, b in ans:
        answer.append(a)

    return answer