def solution(order):
    answer = 0
    stack = []

    for box in range(1, len(order) + 1):
        if box != order[answer]:
            while stack:
                if stack[-1] == order[answer]:
                    answer += 1
                    stack.pop()
                else:
                    stack.append(box)
                    break
            else:
                stack.append(box)
        else:  # 컨테이너 벨트 순서와 주문순서가 같을 때
            answer += 1
    # print(stack,box, answer)
    while stack:
        if stack[-1] == order[answer]:
            answer += 1
            stack.pop()
        else:
            break

    return answer


# 문제풀이
# 탈줄 조건만 잘 잡으면 되는 문제였던것 같은데
# 구체적으로 머리에 그려지지 않았다.