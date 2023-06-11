def solution(price, money, count):
    idx = 1
    total = 0
    for i in range(1,count+1):
        total += price * i
    # print(total)
    if total > money:
        return total-money
    else:
        return 0