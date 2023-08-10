def solution(s):
    temp = s[2:-2].split('},{')
    intTuple = []
    for el in temp:
        intTuple.append(list(map(int, el.split(','))))

    tupleDict = dict()
    for i in intTuple:
        for j in i:
            if j not in tupleDict.keys():
                tupleDict[j] = 1
            else:
                tupleDict[j] += 1
    aa = dict(sorted(tupleDict.items(), key=lambda x: x[1], reverse=True))
    answer = list(aa.keys())
    return answer


## 문제 풀이
# 주어진 문자열을 어떻게 튜플로 만드느냐가 관건이었던것 같다.
# 정수로된 튜플로 만들기 위해 우선 모든 문자열 split을 해주는데
# 문자열 처음과 끝의 괄호를 제외하고, '},{'를 기준으로 우선 잘라서 배열에 저장했다.
# 그리고 그 배열에 있는 문자열 원소를 ','를 기준으로 split하고 정수변환해서 리스트에 저장했다.
# 문제에 따르면, 빈도가 높은 순서대로 튜플이 구성된다.
# 정수변환한 리스트를 하나씩 카운트 해주면서 원소를 key로 하고 빈도를 value로 갖는 딕셔너리를 생성했다.
# value를 기준으로 내림차순으로 정렬하면, 딕셔너리의 키의 순서가 곧 튜플의 순서가 된다.