# N 과 M 3
# 중복 허용 순열
# [1,1],[1,2] ....[2,1],[2,2]

def permu(m, depth,start, arr):
    if depth == m:
        print(*arr)
    else:
        for i in range(start+1, N+1):
            permu(m,depth+1,start,arr + [i])

N,M = map(int, input().split())

permu(M,0,0,[])

# 순열을 만들 때 같은 숫자 중복을 허용하기 위해서는
# depth와 별개로 start 지점을 설정해야한다.
# start는 각 자리의 숫자를 어디서 부터 허용할 것인지 정하는 변수라고 생각하기
