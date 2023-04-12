# 부분 집합으로 풀기


N, S = map(int,input().split())
arr = list(map(int, input().split()))
count = 0
def subset(start, end, P):
    global count,S

    if start == end:
        if len(P) == 0:
            return
        elif sum(P) == S:
            # print(P)
            count += 1
            return
        return

    P.append(arr[start])
    start += 1
    subset(start, end, P)
    P.pop()
    subset(start, end, P)

subset(0,N,[])
print(count)