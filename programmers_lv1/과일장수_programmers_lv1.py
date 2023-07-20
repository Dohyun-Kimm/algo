def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    # print(score)
    boxes = []
    for a in range(m - 1, len(score), m):
        boxes.append(score[a])
        # print('?',a)
    # print(boxes)

    return sum(boxes) * m