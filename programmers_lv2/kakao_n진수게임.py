def solution(n, t, m, p):
    answer = ''
    # n진법으로 m명이 게임할때 p번째 사람이 말해야할 숫자 t개 구하기.
    gamelog = '0'
    cnt = 0
    overDecimal = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    # 게임 진행
    while len(gamelog) < t * m:
        # 말 할 숫자 n진법 변환
        cntToN = []
        tmp = cnt
        while tmp > 1:
            el = tmp % n  # n진법 자릿수
            if el in overDecimal.keys():  # 10 진법 이상일때
                cntToN.append(overDecimal[el])
            else:  # 10진법 이하일때
                cntToN.append(el)
            tmp = tmp // n
        if tmp == 1:
            cntToN.append(tmp)
        gamelog += ''.join(map(str, cntToN[::-1]))
        cnt += 1

    for i in range(p - 1, t * m, m):
        answer += gamelog[i]
    return answer

# 문제풀이
# n진법으로 m명이 게임할때 p번째 사람이 말해야할 숫자 t개 구하기.
# 문제를 한문장으로 정리할 수 있어서 풀이 설계하기 쉬운 편이었다.
# 게임 참가 인원의 모든 대답을 gamelog에 기록하고 p순서에 해당하는 것만 answer에 넣었다.
