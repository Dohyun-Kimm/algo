def is_correct(s):
    stack = []
    stack.append(s[0])
    for i in range(1, len(s)):
        if len(stack) == 0 or stack[-1] == ')' or (stack[-1] == '(' and s[i] == '('):
            stack.append(s[i])
        else:
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


def is_balanced(s):
    chk = 0
    for c in s:
        if c == '(':
            chk += 1
        elif c == ')':
            chk -= 1
    if chk == 0:
        return True
    else:
        return False


def solution(p):
    answer = ''
    u, v = '', ''
    # 빈 문자열이나 올바른 괄호는 그대로 반환
    if len(p) == 0 or is_correct(p): return p

    # u가 균형잡힌 괄호가 될때 까지 2개씩 추가하기
    for i in range(2, len(p) + 1, 2):
        if is_balanced(p[0:i]):
            u = p[0:i]
            v = p[i:len(p)]
            break

    if is_correct(u):
        # u가 올바른 괄호일때
        answer += u + solution(v)
    else:
        # u가 올바른 괄호 문자열이 아닐때
        answer += '(' + solution(v) + ')'
        for c in u[1:-1]:
            if c == '(':
                answer += ')'
            else:
                answer += '('

    return answer