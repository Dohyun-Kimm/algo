def solution(s):
    answer = 0
    first_letter = s[0]
    first_cnt = 1
    other_cnt = 0
    for idx in range(1, len(s)):
        print(first_letter)
        if first_letter:
            if s[idx] == first_letter:
                first_cnt += 1
            else:
                other_cnt += 1
            if first_cnt == other_cnt:
                answer += 1
                first_letter = ''
                first_cnt = 0
                other_cnt = 0
        else:
            first_letter = s[idx]

            first_cnt = 1
    if first_letter != '':
        answer += 1
    return answer