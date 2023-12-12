def solution(storey):
    answer = 0
    divider = 10
    # storey = 965
    while storey > 0:
        last_digit = storey % divider
        # print(storey,'aa')
        if last_digit == 5:
            if storey // 10 % 10 >= 5:
                # print(storey//10%10)
                answer += 10 - last_digit
                storey += 10 - last_digit
            else:
                answer += last_digit
                storey -= last_digit
        elif last_digit > 5:
            answer += 10 - last_digit
            storey += 10 - last_digit
        else:
            answer += last_digit
            storey -= last_digit

        storey = storey // 10
    # print(answer)
    return answer