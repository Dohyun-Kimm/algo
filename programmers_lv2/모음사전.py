def solution(word):
    answer = 0
    for i, n in enumerate(word):
        # print(i,n)
        # print((5 ** (5 - i) - 1) / (5 - 1),i,n)
        # answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
        print((5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n),i,n,answer)
    return answer


# 문제 풀이
# 백트레킹으로 한글자씩 채워서 모든 경우를 만들려고 했는데
# 재귀를 빠져나오지 못해서 실패 했따.
# 문제를 충분히 뜯어보면 생각할 수 있을 법한 풀이가 있어서 참고해서 풀었다.
# 내일은 이 문제를 다시 납득할수 있을만큼 손코딩을 해보고
# 이 풀이를 생각해 낼 수 있는 포인트를 찾아봐야겠다.