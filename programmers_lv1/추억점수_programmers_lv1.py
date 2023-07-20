def solution(name, yearning, photo):
    answer = []
    map_input = dict()
    for a,b in zip(name,yearning):
        map_input[a] = b
    # print(map_input)
    for p in photo:
        score = 0
        for n in p:
            if n not in map_input:
                continue
            else:
                score += map_input[n]
        answer.append(score)
    return answer



#

# def solution(name, yearning, photo):
#     dictionary = dict(zip(name,yearning))
#     scores = []
#     for pt in photo:
#         score = 0
#         for p in pt:
#             if p in dictionary:
#                 score += dictionary[p]
#         scores.append(score)
#     return scores