# N 과 M 1
# 중복 없이 고른 수열
# 증가하는 순서로 출력
# [1,2,3], [1,2,4],[1,2,5], ...
N, M = map(int,input().split())
chosen = [False for _ in range(N+1)]
def permu(depth,m,arr):
    # 순열 완성 되면 출력 하기
    if depth == m:
        print(*arr)
    for i in range(1,N+1):
        if chosen[i] ==False:
            chosen[i] = True
            permu(depth + 1, m, arr + [i])
            chosen[i] = False
permu(0,M,[])

# for 문 조절 -> 순열/조합 구분
# chosen  -> 중복 허용