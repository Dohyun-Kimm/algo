def solution(s):
    if len(s) == 4 or len(s) == 6:
        for c in s:
            # print(c)
            if ord(c) > 64:
                return False
        return True
    else:
        return False
