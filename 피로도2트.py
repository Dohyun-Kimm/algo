# 피로도 다시 풀기
# k : 피로도
# dungeons : [최소피로도, 필요피로도]
# 1. 모든 순열 찾기
# 2. 길이 구하기
# 3. 최대 길이 리턴하기

answer  = -1
checked = []

def permu(k,dungeons,P):
    global answer
    # print(P, answer )
    if len(P) >answer:
        answer = len(P)

    for i in range(len(dungeons)):
        # print('for', i)
        if k >= dungeons[i][0] and checked[i] == False:
            checked[i] = True
            permu(k-dungeons[i][1],dungeons,P+[i])
            checked[i] = False


def solution(k, dungeons):
    global checked, answer
    answer = -1
    checked = [False for _ in range(len(dungeons))]
    permu(k,dungeons,[])
    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))