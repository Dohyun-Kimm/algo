def solution(s, skip, index):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for ss in skip:
        alphabet = alphabet.replace(ss,'')
    # print(alphabet)
    for c in s:
        answer += alphabet[(alphabet.index(c) + index) % len(alphabet)]
    return answer