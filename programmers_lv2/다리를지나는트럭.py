from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)  # 다리 데큐 형태로 선언
    trucks = deque(truck_weights)
    curr_bridge = 0
    time = 0
    # 트럭이 다 지나갈때까지 반복
    while len(trucks) != 0:
        time += 1
        curr_bridge -= bridge.popleft()
        if curr_bridge + trucks[0] <= weight:
            curr_bridge += trucks.popleft()
            bridge.append(curr_bridge)

        else:
            bridge.append(0)

    time += len(bridge)

    return time