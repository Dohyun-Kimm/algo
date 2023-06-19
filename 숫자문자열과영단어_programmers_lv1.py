def solution(s):
    letters = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    temp = ''
    ans_string = ''
    for c in s:

        if c.isdigit():
            ans_string += c
        else:
            temp += c
        if temp in letters:
            ans_string += str(letters.index(temp))
            temp = ''
    # print(ans_string)
    return int(ans_string)
