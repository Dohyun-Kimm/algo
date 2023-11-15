import heapq


def solution(operations):
    answer = []
    queue = []
    for op in operations:
        command, content = op.split()
        print(command, content)
        if command == 'D':
            # 삭제 명령
            if queue and content == '1':
                queue.pop()
            elif queue and content == '-1':
                heapq.heappop(queue)

        else:
            # 삽입 명령
            heapq.heappush(queue, int(content))

    if queue:
        queue.sort()
        return [queue[-1], queue[0]]
    else:
        return [0, 0]
