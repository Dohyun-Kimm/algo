def solution(queue1, queue2):
    answer, i, j = 0, 0, 0
    length = len(queue1) * 2
    q1 = sum(queue1)
    q2 = sum(queue2)

    while q1 != q2:
        if answer > length+1:
            return -1
        if q1 > q2:
            q1 -= queue1[i]
            q2 += queue1[i]
            queue2.append(queue1[i])
            i += 1
        elif q2 > q1:
            q2 -= queue2[j]
            q1 += queue2[j]
            queue1.append(queue2[j])
            j += 1
        answer += 1

    return answer
'''
 큐를 사용 하는 문제라고 되어있지만 큐를 사용하면 시간초과가 나는 문제였다. 
 실제로 배열에서 값을 추가하고 제거하는 과정을 하기보다는 
 두 배열의 합의 변화가 중요하기 때문에 굳이 배열의 변화를 구현하기보다 두배열의 합의 변화만 맞게 변화시키면되는 문제였다.
 두 배열의 합이 같아질수 없는 시점을 정하는것이 중요한 문제였는데, 연산의 횟수가 두배열의 길의합보다 커질때라고 생각했다.
 하지만, 두 배열이 서로 주고 받는과정을 거쳐서 원래의 상태로 돌아오기까지는 두배열의 길이의 합 +1 번 필요하다 
'''

# from collections import deque
#
#
# def solution(queue1, queue2):
#     answer = 0
#     flag1 = queue1[0]
#     flag2 = queue2[0]
#
#     q1 = sum(queue1)
#     q2 = sum(queue2)
#     # total = q1 + q2
#     queue1 = deque(queue1)
#     queue2 = deque(queue2)
#
#     while q1 != q2:
#         # print(queue1,queue2,q1,q2,answer)
#         if answer > 0 and queue1 and queue2:
#             if queue1[0] == flag1 and queue2[0] == flag2 and answer >= len(queue1)+len(queue2):
#                 return -1
#         if q1 > q2:
#             d = queue1.popleft()
#             q1 -= d
#             q2 += d
#             queue2.append(d)
#             answer += 1
#         elif q2 > q1:
#             e = queue2.popleft()
#             q2 -= e
#             q1 += e
#             queue1.append(e)
#             answer += 1
#
#     return answer
#
# # print(solution([1, 1],	[1, 5]))
# print(solution([1, 2, 1, 2],	[1, 10, 1, 2]))
'''
[1, 2, 1, 2],	[1, 10, 1, 2]
[1, 1],	[1, 5]
'''