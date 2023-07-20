# def solution(X, Y):
#     answer = ''
#     x_count = [0] * 10
#     y_count = [0] * 10
#
#     for i in range(9, -1, -1):
#         x_count[i] = X.count(str(i))
#         y_count[i] = Y.count(str(i))
#
#     pairs = []
#     for idx, (i, j) in enumerate(zip(x_count, y_count)):
#         if i and j:
#             pairs += [idx] * min(i, j)
#
#     pairs.sort(reverse=True)
#     answer = ''.join(map(str, pairs))
#
#     if answer:
#         if int(answer):
#             return answer
#         else:
#             return '0'
#     else:
#         return '-1'
#

######################################################
# 정답 풀이

    x_count = [0] * 10
    y_count = [0] * 10
    answer = ''
    for i in range(9, -1, -1):
        x_count[i] = X.count(str(i))
        y_count[i] = Y.count(str(i))

    for j in range(9, -1, -1):
        answer += str(j) * min(x_count[j], y_count[j])

    if answer:
        if answer[0] == '0':
            return '0'
        else:
            # print(answer)
            return answer
    else:
        return '-1'