# N 과 M 2
#

N, M = map(int,input().split())
chosen = [False for _ in range(N+1)]

def combi(m,depth,start,arr):
    if m == depth:
        print(*arr)
    for i in range(start+1, N+1):
        if chosen[i] == False:
            chosen[i] = True
            combi(m,depth+1,i,arr + [i])
            chosen[i] = False

combi(M,0,0,[])

# 오름 차순일때 시작점을 설정 해주기