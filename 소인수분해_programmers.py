def solution(n):
    N = 10000
    cursor = 4
    prime_num = [2, 3]
    answer = []

    while cursor < N:
        for i in prime_num:
            if cursor % i == 0:
                break
        else:
            prime_num.append(cursor)
        cursor += 1
    # print(prime_num)

    for j in prime_num:
        if j > n:
            break
        else:
            if n % j == 0:
                answer.append(j)

    return answer