import heapq


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1  # 작업이 시작되는 시점
    heap = []
    # 처리할 요청이 있으면 반복하기
    while i < len(jobs):
        for j in jobs:
            # heap의 자동정렬 기능 활용하기.0 번 인덱스를 기준으로 자동정렬된다.
            # 다음 작업에 들어갈 수있는 작업들만 heap으에 포함하기
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        # 다음 작업 처리하기
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1

    return int(answer / len(jobs))