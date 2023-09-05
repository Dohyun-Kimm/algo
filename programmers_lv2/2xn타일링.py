def solution(n):
    # 피보나치
    fibonacci = [2, 3]
    if n < 4:
        return n
    else:
        for _ in range(4, n + 1):
            a, b = fibonacci[0], fibonacci[1]
            fibonacci[0], fibonacci[1] = fibonacci[1], a + b
    # print(fibonacci)

    return fibonacci[-1] % 1000000007

# 문제풀이
# 바닥의 길이에 따른 경우의 수를 손으로 계산을 하면서 피보나치 수열이라는것을 깨달았다.
# 피보나치 수열을 전부 배열에 저장하니 런타임 에러가 나서
# 계산에 필요한만큼만 사용했더니 통과되었다.