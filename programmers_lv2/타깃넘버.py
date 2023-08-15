def solution(numbers, target):
    answer = 0

    def dfs(length, result, i):
        nonlocal answer
        nonlocal target

        if i + 1 == len(numbers):
            if result == target:
                answer += 1
                return
        if i + 1 < len(numbers):
            dfs(length + 1, result + numbers[i + 1], i + 1)
            dfs(length + 1, result - numbers[i + 1], i + 1)

    dfs(0, numbers[0], 0)
    dfs(0, -numbers[0], 0)
    return answer

# 문제 풀이
# 모든 경우의 수룰 따져봐야하는 문제.
# dfs로 접근했다. 인덱스가 0일때 + 일경우, - 일경우를 다르게 하여 탐색을 시작했고,
# 각 인덱스마다 +, -를 반영하면서 탬색했다.
# 모든 숫자들에 대해 연산을 끝내고 result가 target과 같으면 answer를 더했다.