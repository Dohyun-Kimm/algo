def solution(data, col, row_begin, row_end):
    answer = 0
    # col번째 칼럼 값을 기준으로 오름 차순 정렬하기, 동일 할땐 첫번째 칼럼 값으로 내림차순
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    # print(data)
    # i 번째 행의 튜플에 대해 각 컬럼의 값을 i로 나눈 나머지들의 합,
    # row_bigin ~ row_end 값까지 S_row_bigin, S_row_end 값 구하기
    result = []
    for i in range(row_begin, row_end + 1):
        s_i = 0
        for j in range(len(data[0])):
            s_i += data[i - 1][j] % i
        result.append(s_i)
    # print(result)

    for a in result:
        answer = answer ^ a
    return answer

'''
  lambda 함수로 오름 차순 내림차순 정렬은 '-'로 정할 수있음.
  XOR 연산은 '^'로 할 수 있음.
'''