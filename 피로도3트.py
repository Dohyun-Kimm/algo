# backtracking으로 풀어보기
# k = 80 dungeons = [[80,20],[50,40],[30,10]]
answer = -1
N = 0
checked =[]

def backtrack( k, dungeons, count):
    global answer,N
    # print('?',count, answer,N)
    if count > answer:
        answer = count

    for i in range(N):
        if k >= dungeons[i][0] and checked[i] == False:
            checked[i] = True
            backtrack(k-dungeons[i][1], dungeons, count+1)
            checked[i] = False


def solution(k, dungeons):
    global answer, checked,N
    answer = -1
    N = len(dungeons)
    checked = [ False for _ in range(N)]
    print(answer,'answer')
    backtrack(k,dungeons,0)
    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))
