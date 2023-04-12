# 1번 수포자 : 1,2,3,4,5
# 2번 수포자 : 2,1,2,3,2,4,2,5
# 3번 수포자 : 3,3,1,1,2,2,4,4,5,5

def solution(answers):
    answer = []
    # 1 3 2 4 2
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    count  = [0,0,0]  # 수포자 별 시험 점수
    for i in range(len(answers)):
        if answers[i] == num1[i%5]:
            count[0] += 1
        if answers[i] == num2[i%8]:
            count[1] += 1
        if answers[i] == num3[i%10]:
            count[2] += 1
    ans = max(count)
    for j in range(3):
        if count[j] == ans:
           answer.append(j+1)
    # print(count)
    return answer

# print(solution([1,2,3,4,5]))