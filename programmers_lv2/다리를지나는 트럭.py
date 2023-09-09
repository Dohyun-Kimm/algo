## 머리 박는 풀이
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 트럭 한 대가 다리르 지나는데 걸리는 시간 : bridge_length
    trucks = deque(truck_weights)
    bridge = deque()  # 현재 다리에 올라와있는 트럭 덱
    seconds = 0
    while True:
        if len(bridge) == bridge_length:
            bridge.popleft()
        if not bridge:
            bridge.append(trucks.popleft())

        elif trucks and trucks[0] + sum(bridge) <= weight:
            bridge.append(trucks.popleft())
            # print(bridge,'???')

        else:
            bridge.append(0)

        seconds += 1
        if sum(bridge) == 0 and len(trucks) == 0:
            break
        # print(bridge)

    return seconds

# 좋다고 생각한 풀이
def solution(length, threshold, trucks):
    answer = 0
    bridge = [0]*length
    cur_weight = 0
    trucks = trucks[::-1]
    while trucks:
        answer += 1
        cur_weight -= bridge.pop(0)
        w = trucks.pop() if cur_weight + trucks[-1] <= threshold else 0
        cur_weight += w
        bridge.append(w)

    return answer + len(bridge)