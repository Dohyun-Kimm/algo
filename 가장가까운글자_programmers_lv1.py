def solution(s):
    answer = []
    stack = []
    for c in s:
        if c not in stack :
            # print(c,'?')
            answer.append(-1)
            stack.append(c)
        else:
            stack.append(c)
            for i in range(len(stack)-1,-1,-1):
                if i != len(stack)-1 and c == stack[i]:
                    # print(c)
                    answer.append(len(stack)-1 - i)
                    break
    return answer