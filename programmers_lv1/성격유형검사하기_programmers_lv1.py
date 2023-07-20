def solution(survey, choices):
    answer = ''
    personality = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for question, choice in zip(survey, choices):
        personality[question[0]] += 4 - choice
    # print(personality)

    if personality['R'] >= personality['T']:
        answer += 'R'
    else:
        answer += 'T'
    if personality['C'] >= personality['F']:
        answer += 'C'
    else:
        answer += 'F'
    if personality['J'] >= personality['M']:
        answer += 'J'
    else:
        answer += 'M'
    if personality['A'] >= personality['N']:
        answer += 'A'
    else:
        answer += 'N'


    return answer