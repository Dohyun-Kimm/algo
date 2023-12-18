# def solution(weights):
#     # 수평을 이루는 길이가 2인 조합 찾기
#     # 한 짝이 가질 수 있는 경우의 수.
#     # (a,b),(2a,3b),(2a,4b),(3a,4b) a>b
#     answer = 0
#     length = len(weights)
#
#     def combi(arr, start):
#         nonlocal answer
#         if len(arr) == 2:
#             # print(arr)
#             bigger, smaller = max(arr), min(arr)
#             if (bigger == smaller) or (bigger * 2 == smaller * 3) or (bigger * 3 == smaller * 4) or (
#                     bigger == smaller * 2):
#                 answer += 1
#             return
#
#         for i in range(start, length):
#             if checked[i] == 0:
#                 checked[i] = 1
#                 combi(arr + [weights[i]], i)
#                 checked[i] = 0
#
#     checked = [0] * len(weights)
#     combi([], 0)
#
#     return answer

# 문제점
# weights의 길이가 10만이 될수 있기 때문에
# 길이가 2인 조합을 먼저 다 찾으려하면, 시간 초과가 나기때문에
# dictionary에  몸무게, 갯수 짝으로 다시 정의

# 정답이 될수 있는 경우의 수
'''
# (a,b),(2a,3b),(2a,4b),(3a,4b) a>b   
먼저 크기가 같은 두원소의 수를 카운트 하기
'''


def solution(weights):
    answer = 0
    dic = dict()
    for w in weights:
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1

    # print(dic)
    for i in dic:
        if dic[i] > 1:
            answer += (dic[i] * (dic[i] - 1)) // 2  # nC2와  같음
        if i * 2 in dic:
            answer += dic[i] * dic[i * 2]
        if i * 2 / 3 in dic:
            answer += dic[i] * dic[i * 2 / 3]
        if i * 3 / 4 in dic:
            answer += dic[i] * dic[i * 3 / 4]
    return answer