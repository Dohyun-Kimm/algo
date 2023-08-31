# def solution(files):
#     # 들어간 숫자들을 정렬하는 배열만들고 인덱스로 files와 연관 시키기
#     trimmedFiles = []
#     for file in files:
#         numberIndex, tailIndex = 0, 0
#         flag = False
#         for i in range(len(file)):
#             if file[i].isdigit() and numberIndex == 0:
#                 numberIndex = i
#                 flag = True
#             elif flag and file[i].isdigit() == False:
#                 tailIndex = i
#                 break
#         trimmedFiles.append([file[:numberIndex], file[numberIndex:tailIndex], file[tailIndex:]])
#     trimmedFiles.sort(key=lambda x: (x[0].lower(), int(x[1])))
#
#     return [''.join(trimmed) for trimmed in trimmedFiles]

# 고친 풀이
def solution(files):
    # 들어간 숫자들을 정렬하는 배열만들고 인덱스로 files와 연관 시키기
    trimmedFiles = []
    for file in files:
        head, num, tail = '', '', ''
        flag = False
        for i in range(len(file)):
            if file[i].isdigit():
                num += file[i]
                flag = True
            elif flag == False:
                head += file[i]
            else:
                tail = file[i:]
                break
        trimmedFiles.append([head, num, tail])
    trimmedFiles.sort(key=lambda x: (x[0].lower(), int(x[1])))

    return [''.join(trimmed) for trimmed in trimmedFiles]

# 배운 것
# 정렬할때 람다를 통해  여러 조건으로 정렬하기
# 문자열 슬라이싱보다는 새로운 문자열을 만들어서 추가하는 것이 시간 복잡도가 낮음
# 슬라이싱 했을때는 런타임 에러가 났지만, 문자열을 더해 주었을 때는 통과가 됨.

