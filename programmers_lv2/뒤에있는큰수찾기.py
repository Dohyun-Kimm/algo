# 	[9, 1, 5, 3, 6, 2]
def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = []
    # 뒷 큰수가 나올 때까지 스택에 저장
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer

# 문제풀이
# 처음엔 numbers를 뒤에서 부터 순회하면서 바로 뒷큰수를 만족하면
# 배열에 추가하고 정답배열에 반영하는 방식으로 구현햇다.
# i번째 수가 바로 뒤의 수보다 크면 정답 배열에 -1을 넣고 배열에 i번째 수를 추가했다.
# i번째 수가 바로 뒤의 수보다 작으면 뒷큰수가 저장된 배열의 마지막 값부터 순회하면서 ..
# 내 첫번째 풀이를 적다보니 풀이가 앞뒤가 맞지 않는다는걸 깨달았따.

# 정답 풀이
# 바로 뒤의 더 큰수가 나올때 까지
# numbers의 인덱스를 슽택에 저장한다.
# 바로 뒤 큰수가 나타나면, stack안에 있던 인덱스들을 pop해서 정답 배열에 반영한다.
# stack이 빈배열이되거나 더 큰수가 없을때까지 반복한다.
# 시뮬레이션을 좀더 침착하게 구체적으로 해봐야겠다....