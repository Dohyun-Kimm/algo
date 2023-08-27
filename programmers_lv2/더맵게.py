# def solution(scoville, K):
#     # 9:20 ~ 10:02
#     answer = 0
#     scoville.sort()
#     i = 0
#     while scoville[i] < K:
#         # scoville 계산
#         if scoville[i] < K:
#             scoville[i + 1] = scoville[i] + scoville[i + 1] * 2
#             scoville[i] = 0
#             i += 1
#             answer += 1
#             # 정렬 유지하기 위해 자리 찾기
#             j = i
#             while j + 1 < len(scoville):
#                 if scoville[j] > scoville[j + 1]:
#                     scoville[j], scoville[j + 1] = scoville[j + 1], scoville[j]
#                     j += 1
#                 else:
#                     break
#
#     return answer

# 문제 풀이
# 스코빌 지수가 낮은 순으로 계산을 하면서
# K이상이 될때까지 두 음식을 합치면서 배열을 업데이트 해나갔다
# 결론적으로는 heap 모듈을 사용하지 않으면 시간 초과가 발생하는 문제같다.


# 2 트
# heap 모듈 사용하기
# impport heapq
# 사용한 method
# heapq.heappush(array, element) , heapq.heappop(array, element)
import heapq


def solution(scoville, K):
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    # print(heap)
    cnt = 0
    while heap[0] < K:
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        cnt += 1

        if len(heap) == 1 and heap[0] < K:
            cnt = -1
            break
    # print(cnt)
    return cnt
