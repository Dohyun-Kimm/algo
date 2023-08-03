def solution(elements):
    answer = 0
    extended = elements + elements[:-1]  # circular queue 펼친 배열
    partialSum_arr = []  # 중복되는 부분수열의 합 확인용

    for i in range(len(elements)):
        for j in range(1, len(elements) + 1):
            if i + j < len(elements):
                partialSum_arr.append(sum(elements[i:i + j]))
            else:
                partialSum_arr.append(sum(elements[i:]) + sum(elements[:i + j - len(elements)]))

    answer = set(partialSum_arr)
    return len(answer)

# 문제풀이
# 모든 연속 부분 수열의 합을 구하되, 끝과 처음이 이어지는 circular queue같은 모양이므로
# 마지막 인덱스를 넘어가는 부분수열의 경우 배열의 길이만큼 빼주어서 다시 첫 인덱스로 돌아가게 코딩함.
# 연속 부분 수열이 배열길이 내에 있을땐 합을 구해서 부분수열합의 배열에 추가해주고,
# 배열길이를벗어나는 인덱스가 있을땐 현재 시작 인덱스~ 배열 마지막 인덱스까지의 합을 구하고,
# 처음 인덱스~ 부분수열의 마지막 인덱스- 배열길이 까지의 합을 구해서 추가해주었다.
# 모든 연속부분수열의합을 구한뒤, 중복 제거를 위해 set()변환 해준뒤 set의 길이를 리턴.

# 인덱스를 다루는 부분이 아직 부족한점이 있다. +1을 해야하는지 안해도되는지 등등
# 포함하고 있는 범위가 내가 의도한 것과 다를때가 있다.
#



