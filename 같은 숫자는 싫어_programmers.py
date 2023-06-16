def solution(arr):
    answer = []
    d = ''
    for c in arr:
        if c != d:
            answer.append(c)
            d = c

    return answer

## Stack 문제인데 stack 사용하지 않음.... 쓸 이유가 없었음... 