# 완탐
# 탐험 조건 : 피로도 > dungeon[0][0]
# 탐험 후 : 피로도 = 피로도 - 소모 피로도.
# 하루에 최대한 탐험을 많이 하는 경우의 수 찾기.
# 백트레킹 이 맞는 듯

import copy
def solution(k, dungeons):
    answer = -1
    # print(dungeons)
    def backtrack(health, arr, i, P,count):
        # print(health,arr,i,P)
        # escape
        global answer
        if health < arr[i][0]:
            if len(P) > count:
                count = len(P)
                answer = count
                print('answer',answer,P)
            return count

        # add dungeons
        # print(arr[i][0])
        if health >= arr[i][0]:
            health -= arr[i][1]  # 소모 피로도 까기
            if health <0:
                if len(P) > count:
                    count = len(P)
                    return count
            P.append(arr[i])  # 탐험한 던전으로 추가
            i += 1  # 다음 인덱스로 이동
            backtrack(health, arr, i, P,count)  # 해당 인덱스 포함한 경우
            P.pop()
            backtrack(health, arr, i, P,count)  # 포함 하지 않는 경우

    backtrack(k,dungeons,0,[],answer)
    return answer




print(solution(80,[[80,20],[50,40],[30,10]]))
