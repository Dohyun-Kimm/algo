import math


def solution(progresses, speeds):
    answer = []
    arr = list(map(lambda x: math.ceil((100 - x[0]) / x[1]), zip(progresses, speeds)))
    functions = []
    for el in arr:
        if not functions:
            functions.append(el)
            completed = 1
        elif el <= functions[-1]:
            completed += 1
        else:
            answer.append(completed)
            functions.append(el)
            completed = 1
    answer.append(completed)

    return answer

# 문제풀이
# 이 문제에서 중요한 점은, 우선순위가 높은 기능이 배포되기까지 다른 기능들은 완성되더라도 배포될수 없다는 것이다.
# 주어진 progresses, speeds를 가지고 각 기능이 완성되기까지의 시간을 배열로 만들었다.
# 완성되기까지의 소요시간이 더 큰 기능이 나타나기 전까지의 모든 기능은 같은 날에 한번에 배포된다.
# 그 기능의 개수를 카운트해주고, 소요시간이 더 긴 기능이 나왔을때 완성된 기능을 정답 배열에추가했다.
# 반복문을 마치면, 마지막 기능을 정답 배열에 추가해주면 된다.