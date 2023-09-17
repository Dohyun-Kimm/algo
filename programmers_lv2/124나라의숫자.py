'''
def solution(n):
    # 3으로 나눈 나머지를 인덱스에 대응 시키면 된다.
    digits = ' 124'
    # print(len(digits), digits)
    # n=14
    answer = ''
    e = 0
    d = n
    while n > 0:

        d = n % 3
        n = n // 3
        if d == 0: d = 3
        if answer and answer[-1] == '4':
            answer += digits[d - 1]
        else:
            answer += digits[d]
    answer = answer.strip()
    return answer[::-1]
'''

def solution(n):
    # 3으로 나눈 나머지를 인덱스에 대응 시키면 된다.
    digits = ' 124'
    # print(len(digits), digits)
    # n=14
    answer = ''
    e = 0
    n = int(n)
    while n >0:
        if n % 3 == 0:
            answer += '4'
            n = n//3-1
        else:
            d = n % 3
            answer += str(d)
            n = n//3

    return answer[::-1]
