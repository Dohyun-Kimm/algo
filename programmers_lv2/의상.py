def solution(clothes):
    answer = 1
    clothHash = dict()
    for cloth in clothes:
        if cloth[1] in clothHash.keys():
            clothHash[cloth[1]].append(cloth[0])
        else:
            clothHash[cloth[1]] = [cloth[0]]
    print(clothHash)
    cntArr = []
    for key in clothHash.keys():
        cntArr.append(len(clothHash[key]))
    print(cntArr)
    if len(cntArr) <2:
        answer  = cntArr.pop()
    else:
        for c in cntArr:
            answer *= (c+1)
        answer -=1
    return answer


# 문제풀이
# 주어진 의상을 종류별로 정리하고 각 항목들중 가능한 모든 조합의 수를 찾으면된다.
# 의상의 종류가 하나일땐 의상의 수가 경우의 수 전체기때문에 그대로 리턴했고
# 2개 이상인 경우엔 의상 종류마다 (의상 개수 +1)를 서로 곱한뒤 1를 빼주면된다.
# 적어도 하나의 의상은 입어야 하기때문에 아무 의상이 선택되지 않았을 경우를 빼주는 것이다.
