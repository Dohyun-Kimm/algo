def solution(n):
    m = n + 1
    nn = str(bin(n))[2:]
    ones = nn.count('1')

    while True:
        mm = str(bin(m))[2:]
        m_ones = mm.count('1')
        if m_ones == ones:
            return m
        else:
            m += 1


# 문제 설명
# 정수를 이진수로 변환하는 문제였다.
# 조건 1) 주어진 수를 이진수로 변환 했을 때 1의 개수가 같음
# 조건 2) 주어진 수 보다 큰 자연수.

# 풀이.
# 조건에 맞게 bin()으로 이진수변환
# 변환 했을때 0b 가 앞에 붙는 다는 것을 고려해서 str() 변환하고 2번째 인덱스부터 처리
# 문자열로 변환된 수에서 1의 개수 찾기
# 주어진 수의 1의 개수와 같은 더큰 수 나올때 까지 반복