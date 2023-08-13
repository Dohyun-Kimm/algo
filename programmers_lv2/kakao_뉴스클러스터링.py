def solution(str1, str2):
    # 자카드 유사도 = 교집합 / 합집합, 공집합일때는 1
    #  65536
    strSet1 = [str1[i:i+2].upper()   for i in range(len(str1)-1) if str1[i:i+2].isalpha() ]
    strSet2 = [str2[i:i+2].upper() for i in range(len(str2)-1)if str2[i:i+2].isalpha() ]
    union = []
    intersection = []
    total = strSet1 + strSet2
    if len(total) == 0:
        return 65536
    else:
        for el in set(total):
            if el in strSet1 and el in strSet2 :
                intersection += [el]*min(strSet1.count(el),strSet2.count(el))
                union += [el]*max(strSet1.count(el),strSet2.count(el))
            else:
                union += [el]*max(strSet1.count(el),strSet2.count(el))
    return int(len(intersection)/len(union)*65536)

# 문제풀이
# 중복된 문자열이 있을때 교집합, 합집합을 구하는 것이 중요 했던 문제같다.
# 우선 isalpha()를 통해 알파벳으로만 이루어진 원소를 구별했고
# isupper()을 통해 통일 시켜주었다.
# 만들어진 두 배열에서 중복 없이 모든 원소를 담은 집합 total을 생성해주고
# 순회 하면서 intersection과 union을 구해주었다.

# 좋다고 생각한 다른 사람의 풀이
# 연산량이 훨씬 적은 코드라고 생각한다.
# import re
# import math
#
# def solution(str1, str2):
#     str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
#     str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]
#
#     gyo = set(str1) & set(str2)  # 잊고있었던 코드였다.
#     hap = set(str1) | set(str2)
#
#     if len(hap) == 0 :
#         return 65536
#
#     gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
#     hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])
#
#     return math.floor((gyo_sum/hap_sum)*65536)