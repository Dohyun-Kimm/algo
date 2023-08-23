def solution(record):
    answer = []
    uidDict = dict()
    log = []
    for r in record:
        # print(uidDict, answer)
        if r.startswith('Leave'):
            case, user = r.split()
            answer.append([user, 'Leave'])
        else:
            case, user, name = r.split()
        if case == 'Enter':
            uidDict[user] = name
            answer.append([user, 'Enter'])
        elif case == 'Change':
            uidDict[user] = name
    for ans in answer:
        if ans[1] == "Leave":
            log.append(uidDict[ans[0]] + '님이 나갔습니다.')
        else:
            log.append(uidDict[ans[0]] + '님이 들어왔습니다.')
    # print(log)
    return log

# 문제 풀이
# 주어진 record를 Leave, Enter, Change일때 각각에 맞는 명령을 수행하게 했다.
# 첫 번째 반복문에서 유저 아이디와 입출입 여부를 answer에 저장하고,
# change일 경우에는 userdict에서 닉네임 정보를 업데이트 했따.
# 두번째 반복문에서 문제에서 요구하는 형태의 답으로 answer를 변환하여 log에 저장했다.
# f string썼으면좀더 보기 ㅂ편했을 수 도