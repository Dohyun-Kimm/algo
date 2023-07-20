def solution(s):
    ans = ''
    p = 0
    for c in s:
        if c == ' ':
            ans+=' '
            p = 0
            continue
        elif p%2:
            p+=1
            ans+= c.lower()
        else:
            p+=1
            ans += c.upper()
    return ans