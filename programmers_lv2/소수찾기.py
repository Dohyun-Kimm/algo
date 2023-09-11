# 소수인지 판별하는 함수
def isPrime(n):
    if n <= 1:
        return False
    if n in [2, 3, 5, 7]:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = set()
    length = len(numbers)

    # 조합 만들기
    def bfs(start, permu):
        nonlocal answer
        checked[start] = 1
        print(permu)
        if isPrime(int(permu)):
            # print(permu)
            answer.add(int(permu))
        for i in range(len(numbers)):
            if checked[i] == 0:
                checked[i] = 1
                bfs(start, permu + numbers[i])
                checked[i] = 0

    for n in range(length):
        checked = [0 for _ in range(length)]
        bfs(n, numbers[n])
    return len(answer)

# itertools를 쓰기가 너무 싫었다.
# 구현할 줄 알아야 모듈을 쓰는것이 의미가 있다고 생각해서 직접 구현하려고했다.
# 사실 bfs를 구현한 것은 아니지만 기본적인 백트레킹을 구현해서 완전탐색이 가능한 함수를 썼다.
# 제약 조건이 없이 순열을 만드는 것이라 난이도가 높은 것은 아니라고 생각했지만, 오랜만에 재귀로 구현하려고하니 생각이 꼬여서 잘 안됐다.
#