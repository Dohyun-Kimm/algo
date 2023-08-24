def solution(land):
    answer = 0
    dp = land
    for i in range(1, len(land)):
        for j in range(len(land[0])):  # j 번쨰 인덱스를 제외한 최대값
            dp[i][j] += max(dp[i - 1][:j] + dp[i - 1][j + 1:])

    # print(dp)

    answer = max(dp[-1])
    return answer

# 문제풀이
# 다이나믹 프로그래밍을 사용해야할 때를 알 수 있었던 문제
# dp의 가장 단순한 활용 문제라고 생각했다.
# 다시 풀어보기
