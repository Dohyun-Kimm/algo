def solution(sequence, k):
    answer_arr = []
    left, right = 0, 0
    current_sum = 0

    while right < len(sequence):
        current_sum += sequence[right]

        while current_sum > k:
            current_sum -= sequence[left]
            left += 1

        if current_sum == k:
            answer_arr.append([left, right])

        right += 1

    shortest = len(sequence)
    answer = []

    for i in answer_arr:
        if i[1] - i[0] < shortest:
            shortest = i[1] - i[0]
            answer = i

    return answer
