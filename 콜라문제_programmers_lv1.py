def solution(a, b, n):
    answer = 0
    # a,b,n = 5,2,22
    while n >= a:
        extra_coke = n % a
        new_coke = n // a
        answer += new_coke * b
        n = new_coke * b + extra_coke
        print(extra_coke)
    # print(answer)

    return answer