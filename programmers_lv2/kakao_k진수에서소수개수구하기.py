def solution(n, k):
    count = 0
    # k 진수로 바꾸기
    nTok = []
    while n > k:
        nTok.append(n % k)
        n = n // k
    if n:
        nTok.append(n)
    kString = ''.join(map(str, nTok))[::-1]
    arr = kString.split('0')

    # 소수 찾기
    for el in arr:
        if el.isnumeric() and int(el) > 1:
            tmp = int(el)
            if tmp <= 3:
                count += 1
            else:
                i = 5
                flag = 0
                if tmp % 2 == 0 or tmp % 3 == 0:
                    flag = 1
                else:
                    while i * i <= tmp:
                        if tmp % i == 0 or tmp % (i + 2) == 0:
                            flag = 1
                            break

                        else:
                            i += 6
                if flag == 0:
                    count += 1

    return count

# 문제 풀이
# 풀이과정을 3 단계로 나누었다.
# 첫 번째는 주어진 수를 k 진수로 바꾸는 것.
# 두 번째는 k진수로 바꾼 문자열을 0을 기준으로 split한 배열에 담는것.
# 세 번째는 배열의 원소들을 10진수로 변환하고 소수인지 판별하는 것.
# 소수를 판별하는 과정에서 에라토스테네스의 체를 사용하지 않고 이중 for문을 사용했을때 1번 테스트 케이스 시간초과가 났다.
# 에라토스테네스의 체를 사용하면 계산량이 줄어들어 시간초과가 나지 않았음
# 하지만  5이상의 소수로 소수 판별 하기 때문에 , 2와 3의 합성수의 경우 판별이 되지 않는 경우가 생김.
# 따라서 while문에 들어가기전, 2와 3으로 한번씩 나눠보고 안나눠지면, while문에 들어가도록함.