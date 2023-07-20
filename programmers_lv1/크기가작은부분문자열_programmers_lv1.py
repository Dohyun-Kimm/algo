def solution(t, p):
    n = len(p)
    pp = int(p)
    answer = 0
    # print(pp)
    for i in range(len(t)-n+1):
        tt=int(t[i:i+n])
        if tt <= pp:
            answer += 1
    return answer