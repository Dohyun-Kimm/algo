# 촌수 계산
# dfs
# 230422

# 출력 조건 : 촌수 계산 가능  할때 몇촌인지 출력
#           불가능 할때 -1

def dfs (start, end, c):
    global answer
    visited[start] = 1
    # print(start,end, c)
    if start == end:
        if not answer and  c < answer :
            answer = c
        elif answer == 0:
            answer = c
        # print(c,"??")
        answer = c
    if answer == 0:
        for j in family[start]:
            if not visited[j]:
                dfs(j, end, c +1)


N = int(input())
s, e = map(int, input().split())
M = int(input())
family = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

count = 0
for i in range(M):
    u,v = map(int,input().split())
    family[u].append(v)
    family[v].append(u)
# print(family)
answer = 0
dfs(s, e, count)
if answer:
    print(answer)
else:
    print(-1)
