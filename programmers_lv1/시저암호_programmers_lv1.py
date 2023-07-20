def solution(s, n):
    lower_ch = 'abcdefghijklmnopqrstuvwxyz'
    upper_ch = lower_ch.upper()
    ordZ = ord('Z')
    ordz = ord('z')
    ordA = ord('A')
    orda = ord('a')

    answer = []
    for c in s:
        if c.isupper():
            temp = ord(c) + n
            if ordA <= temp <= ordZ:
                answer.append(chr(temp))
            else:
                answer.append(chr(ordA + (temp - ordZ) - 1))
        elif c.islower():
            temp = ord(c) + n
            if orda <= temp <= ordz:
                answer.append(chr(temp))
            else:
                answer.append(chr(orda + (temp - ordz) - 1))
        if c == ' ':
            answer.append(' ')

    return ''.join(answer)