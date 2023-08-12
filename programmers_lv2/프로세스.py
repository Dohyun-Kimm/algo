from collections import deque


def solution(priorities, location):
    completed = []
    queue = deque(priorities)
    processes = deque([i for i in range(len(priorities))])
    while True:
        q = queue.popleft()
        p = processes.popleft()
        # print(p)
        if not queue:
            # print('?')
            break
        for process in queue:
            if process > q:
                queue.append(q)
                processes.append(p)
                break
        else:
            completed.append(p)  # 인덱스를 추가해주기

    completed.append(p)
    # print(completed)
    # print(completed.index(location))

    return completed.index(location) + 1

# 문제풀이
# 문제에서 알려주는 프로세스 처리 알고리즘을 그대로 구현하려고 했다.
# 우선순위가 담긴 배열을 deque로 새로 담고 우선수위를 가리키는 인덱스를 processes라는 deque에 담았다.
# 앞에서부터 pop해서 나온 프로세스보다 우선순위가 높은 프로세스가 deque에 있으면 다시 맨뒤에 넣고
# 없으면 completed에 추가했다.
# 위 과정을 deque가 빌때까지 반복하면 전체 프로세스 처리 결과가 나오고, completed에서 location위치의 인덱스 +1 해주면된다.
