def solution(participant, completion):
# 시간 초과 발생한 코드
    # hash_map = { chr(i) : []  for i in range(97,123)}
    # for c in completion:
    #     hash_map[c[0]].append(c)
    # for p in participant:
    #     if p in hash_map[p[0]]:
    #         hash_map[p[0]].remove(p)
    #     else:
    #         return p

# 시간초과 발생하지 않은 코드.
    participant.sort()
    completion.sort()
    # print(participant,completion)
    for idx, c in enumerate(completion):
        if c != participant[idx]:
            return participant[idx]
    else:
        return participant[-1]

