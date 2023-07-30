def solution(arr):
    # 두개씩 비교해서 최소공배수 뽑기
    # 최대 공약수 구하는 함수
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # 최소 공배수 구하기
    def lsm(c, d):
        return (c * d) // gcd(c, d)

    lsmArr = [arr[0]]
    temp = arr[0]
    for i in range(1, len(arr)):
        temp = lsm(temp, arr[i])
        # print(temp)
    return temp
