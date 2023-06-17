def solution(number):
    answer = []
    checked = [False for _ in range(len(number))]

    def combi(length, start, arr):
        if len(arr) == 3 and sum(arr) == 0:
            answer.append(arr)
            return arr
        for i in range(start, len(number)):
            if not checked[i]:
                checked[i] = True
                combi(length, i, arr + [number[i]])
                checked[i] = False

    combi(3, 0, [])
    return len(answer)