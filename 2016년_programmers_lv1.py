def solution(a, b):
    # a, b = 3,1
    dow = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = (a - 1) * 31 + b
    # print(days)
    minus_day = 0
    month_30s = [4, 6, 9, 11]
    for i in range(1, a):
        if i == 2:
            minus_day += 2
            # print('a')
        elif i in month_30s:
            minus_day += 1
            # print('b')
    result = (days - minus_day) % 7

    answer = dow[result - 1]
    # print(result)
    return answer