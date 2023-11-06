# 2023.03. fail
# def solution(numbers):
#     answer = ''
#     # 배열의 각 원소를 천 이하의 수로 만든다.
#     # 자릿 수를 늘린 수의 크기를 비교해서 재정렬 한뒤 원상 복구
#     # 배열을 문자열로 만들면돼
#     newNums = dict()
#     for  i, n in enumerate(numbers) :
#         if n < 10:
#             newNums[i] = n *100
#         elif n < 100:
#             newNums[i] = n * 10
#         elif n == 1000:
#             newNums[i] = n // 10
#         else:
#             newNums[i] = n
#     sortedDict =dict(sorted(newNums.items(), key=lambda x : x[1], reverse=True))
#     # print(sortedDict)
#     for key in sortedDict:
#         answer += str(numbers[key])
#
#     # print(answer)
#
#     return answer


# 저답 풀이
def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))  # string으로 바꾸어서 비교
    numbers.sort(key=lambda x: x * 3, reverse=True)  # 3번씩 반복하면 붙였을때 큰수 찾기 가능

    for i in numbers:  # 정렬된 리스트를 answer에 순서대로 더해줌
        answer += i

    return str(int(answer))
'''
 원소 값을 3번 반복해주는 것이 중요했음.
 30,3, 39 라는 숫자가 있다고 가정했을때 올바른 순서는 39330이다
 하지만 크기로 정렬하면 39303이된다
 이를 해결하기위해 각 원소를 3번 반복한뒤 정렬한다
 303030, 333, 393939를 정렬하면
 393939,333,303030 이 된다. 이 수식을 lambda에 조건으로 주는 풀이.
'''