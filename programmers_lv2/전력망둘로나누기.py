# 못푼 문제
# 다른 사람의 풀이 분석
'''
dfs를 이용해 한 트리의 속해있는 자식 노드의 개수를 구하는 방법
-> 전체 노드개수가 정해져있기 때문에 나눠진 한쪽 트리 개수만 구하면 됨.

def dfs(cur,wires,ch):
    global tmp

    for i in range(len(ch)-1):
        if ch[i] ==0:
            for j in range(2):
                if wires[i][j] == cur:
                    ch[i] = 1
                    tmp + =1
                    dfs(wires[i][j+1%2],wires,ch)
                    ch[i]= 0

dfs solution(n, wires):
    ch = [0] *n
    res = []
    global tmp

    for i in range(n-1):
        tmp = 1     # 노드의 수 1개로 시작
        ch[i] =1    # 방문 여부
        a,b = wires[i][0], wires[i][1]

        dfs(a,wires,ch)
        ch[i] = 0
        res.append(abs(2*tmp -n))
    return min(res)
'''