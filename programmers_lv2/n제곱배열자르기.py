def solution(n, left, right):
    answer = []
    # arr = [0] * (n**2)
    # temp = [[0 for _ in range(n)] for _ in range(n)]
    count = 0
    # for i in range(1,n+1):
    #     for j in range(1,n +1):
    #         tmp = 0
    #         if j <= i:
    #             tmp = i
    #             # temp[i-1][j-1] = i
    #         else:
    #             tmp = j
    #             # temp[i-1][j-1] = j
    #         if left <= count <=right:
    #             answer.append(tmp)
    #         count+=1
    for i in range(left,right+1):
        a = i // n
        b = i % n
        answer.append(max(a,b)+1)
    # print(answer)
    return answer


# 배열이 채워지는 규칙을 이해하고 떠올리는데 오래걸렸다.
# 왜 오래걸렸지.....
# 쉽게 풀수도 있었는데 아쉽다