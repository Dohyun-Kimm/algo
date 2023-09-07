def solution(numbers):
    answer = []
    for n in numbers:
        bit_n = bin(n)
        length = len(bit_n[2:])
        print(length,'qwer')
        for i in range(n+1,1<<n):
            print(i,i|n)
    return answer

# 문제풀이
# 주어진 숫자 n을 비트연산을 해서
# n 보다 큰수들중에 n 과 다른 자리수를 하나하나 체크 하려고 했음....

# 다른 사람의 풀이
def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
            continue

        number_bin = '0' + bin(number)[2:]
        number_bin = number_bin[:number_bin.rindex('0')] + '10' + number_bin[number_bin.rindex('0') + 2:]
        answer.append(int(number_bin, 2))

    return answer

# 피드백
# 문제 자체를 깊이 파보려고 하지 않았던것 같다.
#