def solution(n, words):
    answer = []
    stack = []
    person = 1
    cycle = 1
    last_word = ''
    for word in words:

        if word not in stack:
            if last_word and word[0] != last_word[-1]:
                return [person, cycle]
            else:
                stack.append(word)
                last_word = word
        else:

            return [person, cycle]

        if person == n:
            person = 1
            cycle += 1
        else:
            person += 1
        # print(person)
    else:
        return [0, 0]



