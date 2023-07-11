def solution(keymap, targets):
    answer = []
    # A - 1, B-1, C-2, D-5, E -3, F-4
    # keymap = ["ABCE"]
    # targets = ["ABCD"]
    real_keymap = dict()
    for k in keymap:
        for i in range(len(k)):
            if k[i] not in real_keymap.keys():
                real_keymap[k[i]] = i + 1
            else:
                if real_keymap[k[i]] > i + 1:
                    real_keymap[k[i]] = i + 1
    print(real_keymap)
    for target in targets:
        count = 0
        for t in target:
            if t not in real_keymap.keys():
                count = -1
                break
            else:
                count += real_keymap[t]

        answer.append(count)

    # print(answer)
    return answer