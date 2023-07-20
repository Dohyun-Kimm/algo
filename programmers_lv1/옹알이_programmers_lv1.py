def solution(babbling):
    answer = 0
    stack = ''
    babble_list = ["aya", "ye", "woo", "ma"]

    for babble in babbling:
        word = ''
        cnt = 0
        babble_stack = []
        for character in babble:
            word += character
            if word in babble_list:
                # print(babble_stack)
                if babble_stack:
                    previous_babble = babble_stack.pop()
                    if word == previous_babble:
                        # print(word)
                        cnt = 0
                        break
                    else:
                        babble_stack.append(word)
                        cnt += 1
                        word = ''

                else:
                    babble_stack.append(word)
                    cnt += 1
                    word = ''
        if cnt and len(word) == 0:
            answer += 1
    return answer