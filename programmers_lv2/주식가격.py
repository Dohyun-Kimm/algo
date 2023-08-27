def solution(prices):
    length = len(prices)
    answer = [0 for _ in range(length)]
    # stack 문제

    stack = []
    for day, price in enumerate(prices):
        if stack:
            if price >= stack[-1][1]:
                stack.append((day, price))
            else:
                while True:
                    prev_day, prev_price = stack.pop()
                    answer[prev_day] = day - prev_day
                    if prev_price <= price:
                        stack.append((prev_day, prev_price))
                        break
                stack.append((day, price))
        else:
            stack.append((day, price))
    # print(stack)
    while stack:
        s = stack.pop()
        answer[s[0]] = length - 1 - s[0]
    return answer

#  문제 풀이
# 가격이 증가 추세일때는 스택에 넣고
# 감소할때 마다 스택의 내용과 비교하면서, 가격이 감소하지 않은 기간을 계산 했다.
# 런타임 에러가 발생함.... 다른 풀이 방법이생각이 안나서 포기
# 주말에 다시 풀기

# 다른 사람의 풀이를 보고 나서 느낀점.
# 시간 복잡도 계산을 정확하게 하지도 않고 효율적인 풀이를 찾으려고하는데에 너무
# 몰두 되었던 것 같다.
# 일단 시키는 대로 풀이를 하려고 하면 문제이해를 명확하게 하는데에도 도움이 되는 것 같다.

# 참고한 풀이이
# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             answer[i] += 1
#             if prices[i] > prices[j]: break
#     return answer

def solution(prices):
    count = [0 for _ in range(len(prices))]
    for p in range(len(prices)):
        for q in range(p + 1, len(prices)):
            count[p] += 1
            if prices[q] < prices[p]:
                break

    # print(count)
    return count
# 2번째 시도
# 유지되는 가격은 마지막날을 제외하고 기본 값이 1일이다.