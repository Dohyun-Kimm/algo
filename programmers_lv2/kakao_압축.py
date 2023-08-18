def solution(msg):
    answer = []
    LZW = ['']
    for i in range(26):
        LZW.append(chr(i + 65))

    start = 0
    end = 1
    while start < len(msg):
        if start == len(msg) - 1:
            print(start)
            break
        if msg[start:end] in LZW:
            end += 1
        else:
            LZW.append(msg[start:end])
            answer.append(LZW.index(msg[start:end - 1]))
            start = end - 1
            end = start + 1

    return answer
# 문제 풀이
# 사전에 없는 문자열이 나올때까지 주어진 메세지를 한글자씩 추가해서 비교하고
# 사전에 없는 문자열이 나왔을때 그 직전 문자열을 사전에 등록했다.
# 이런식으로 풀어나가면 마지막 문자열이 추가되지 않는다...

# 정답 풀이
def solution1(msg):
    answer = []
    eng = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

    while len(msg) > 0:
        w = msg[0]
        cnt = 0
        if len(msg) == 1:
            answer.append(eng.index(w) + 1)
            break
        while len(w) < len(msg):
            s = w
            cnt += 1
            w += msg[cnt]
            if w not in eng:
                w = s
                break
        answer.append(eng.index(w) + 1)
        msg = msg[len(w):]
        if msg:
            eng.append(w + msg[0])
    return answer