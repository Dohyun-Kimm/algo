def solution(want, number, discount):
    answer = 0
    wishList = dict()
    for w, n in zip(want, number):
        wishList[w] = n

    length = sum(number)
    for i in range(len(discount)):
        if i + length < len(discount) + 1:
            discountDay = discount[i:i + length]
            for j in range(length):
                if discountDay[j] not in wishList.keys():
                    break
                elif discountDay.count(discountDay[j]) != wishList[discountDay[j]]:
                    break
            else:
                answer += 1
    return answer

# 문제풀ㅇ이
# 구현 문제라고 판단했다.
# 원하는 물건과 수량을 한번에 보기 위해서 dict로  want 와 number을 묶어주었다. (=wishList)
# number의 총 합만큼 할인행사를 활용해야 하기때문에 discount를 number 총합만큼 잘라서 부분 배열을 탐색했다.
# 물건을 하나라도 살수 없으면 회원가입을 안하기 때문에
# wishList에 없거나 수가 안맞으면 바로 break해서 계산을 최소화 하려고 했다.
