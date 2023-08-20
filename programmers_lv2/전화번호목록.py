def solution(phone_book):
    phone_book.sort()
    idx = 0
    answer = True
    while idx < len(phone_book):
        head = phone_book[idx]
        j = idx + 1
        if j < len(phone_book) and head == phone_book[j][:len(head)]:
            answer = False
            break
        else:
            idx += 1
    return answer

# 문제설명
# 전화번호 리스트 중에서 다른 전화번호의 접두어가 되는 번호가 있는지 확인하는 문제
# 어떻게 접근할지 몰라서 못푼 문제
# 0820 다시 풀이
# 전화번호 목록을 처음에 정렬하는 것이 문제풀이를 쉽게 만들었다. 문자열이 들어있는 배열을 정렬하면
# 사전적으로 앞에있으면서 길이가 짧은 문자열이 앞으로 정렬되기 때문에 접두어가 되는 번호를 적은 계산으로 찾을 수있었다.





# 다른 사람의 풀이
# 정렬을 했다.
# 정렬을 한뒤, 하나씩 비교하면서 풀었다.
# 접두어가 되는지 확인 하는 메소드 startwith()
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True