def solution(n):
    # 3으로 나눈 나머지를 인덱스에 대응 시키면 된다.
    digits = '412'
    # n=14
    answer = ''
    while n >0:
        d = n % 3
        n = n//3
        answer += digits[d]
    # print(answer[::-1])
    return answer[::-1]