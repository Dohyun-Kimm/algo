def solution(dartResult):
    star, acha = '*', '#'
    multiplier = ['S', 'D', 'T']
    point = []
    for idx, c in enumerate(dartResult):
        if c.isdigit():
            if dartResult[idx + 1] == '0':
                point.append(10)
            elif c == '0' and dartResult[idx - 1] == '1':
                continue
            else:
                point.append(int(c))


        elif c in multiplier:
            if c == 'S':
                point.append(point.pop())

            elif c == 'D':
                point.append(point.pop() ** 2)
            else:
                point.append(point.pop() ** 3)
        else:
            if c == acha:
                point[-1] = point[-1] * (-1)

            else:
                point[-1] = point[-1] * 2
                if len(point) > 1:
                    point[-2] = point[-2] * 2

    print(point)
    return sum(point)