def solution(arrayA, arrayB):
    # 각 배열에 대해서 공약수의 집합을 구하기
    # 최대 공약수 부터 상대 배열에 나누기 하나라고 안나눠지면 정답에 추가
    # 공약수 구하기
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd_a, gcd_b = arrayA[0], arrayB[0]
    for i in range(1, len(arrayA)):
        gcd_a = gcd(gcd_a, arrayA[i])
    for j in range(1, len(arrayB)):
        gcd_b = gcd(gcd_b, arrayB[j])
    result_a = gcd_a
    result_b = gcd_b

    for b in arrayB:
        if b % gcd_a == 0:
            result_b = gcd_a // gcd(b, gcd_a)
    for a in arrayA:
        if a % gcd_b == 0:
            result_a = gcd_b // gcd(a, gcd_b)
    # print(gcd_a, gcd_b)
    # 상대 배열에 나눠보기

    # print(a_div,b_div)
    for b in arrayB:
        if b % gcd_a == 0:
            gcd_a = gcd_a // gcd(b, gcd_a)
    for a in arrayA:
        if a % gcd_b == 0:
            gcd_b = gcd_b // gcd(a, gcd_b)

    if gcd_a == gcd_b:
        return 0
    else:
        return max(gcd_a, gcd_b)