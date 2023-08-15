# 문제설명
# 전화번호 리스트 중에서 다른 전화번호의 접두어가 되는 번호가 있는지 확인하는 문제
# 어떻게 접근할지 몰라서 못푼 문제

# 다른 사람의 풀이
# 정렬을 했다.
# 정렬을 한뒤, 하나씩 비교하면서 풀었다.
# 접두어가 되는지 확인 하는 메소드 startwith()
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True