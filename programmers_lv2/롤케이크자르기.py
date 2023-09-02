def solution(topping):
    answer = 0
    dict1 = dict()
    for t in topping:
        if t not in dict1:
            dict1[t] = 1
        else:
            dict1[t] += 1

    dict2 = dict()
    for t in topping:
        if len(dict1) == len(dict2):
            answer += 1
        if t not in dict2:
            dict2[t] = 1
        dict1[t] -= 1
        if dict1[t] == 0:
            del dict1[t]
    return answer
# 단순하게 풀자

# 풀이 1
# 문제가 어렵다고 생각해서 어렵게 접근하다보니 생각보다 간단하다는 것을 알아차리지 못했다.
# 주어진 배열을 두개로 나누고 그 개수가 같을때마다  카운트만 해주면 되는 문제였다.
# def solution(topping):
#     answer = 0
#     # 양쪽 개수가 똑같아 질때 까지 이분 탐색
#     # 끝 까지 가면 return 0
#     length = len(topping)
#     start = len(topping) // 2
#
#     def search(idx, cnt, root):
#         nonlocal answer, length
#         right, left = len(set(topping[:idx])), len(set(topping[idx:]))
#         # print(idx,cnt,root, right, left)
#         # 이분 탐색이 양쪽 끝에 닿았을때
#         if idx == 0 or idx == len(topping) - 1:
#             answer += cnt
#             return
#         elif cnt > 0 and right != left:
#             answer += cnt
#             return
#             # 양쪽 종류의 수가 같아졌을때
#         if right == left:
#             cnt += 1
#             if idx + 1 > root:
#                 search(idx + 1, cnt, idx)
#             elif idx - 1 < root:
#                 search(idx - 1, cnt, idx)
#         elif right > left:
#             search((length - idx) // 2, cnt, root)
#         else:
#             search(idx // 2, cnt, root)
#
#     search(start, 0, start)
#     return answer
