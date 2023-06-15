def solution(n, m):
    gcd, mcm = 1, 1
    nm = n * m
    bigger = max(n, m)
    smaller = min(n, m)
    for i in range(1, smaller + 1):
        if nm % i == 0 and smaller % i == 0 and bigger % i == 0:
            gcd = i
            mcm = int(nm / i)

    answer = [gcd, mcm]
    return answer


###  Euclidian 호제법?

# def gcdlcm(a, b):
#     c,d = max(a, b), min(a, b)
#     t = 1
#     while t>0:
#         t = c%d
#         c, d = d, t
#     answer = [ c, int (a*b/c)]
#     return answer
#
# print(gcdlcm(3,12))