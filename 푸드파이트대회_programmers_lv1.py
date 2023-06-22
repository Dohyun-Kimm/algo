def solution(food):
    answer = ''
    left = ''
    for a in range(len(food)):
        if food[a] % 2 :
            food[a] = food[a]-1
    # print(food)
    for i in range(1,len(food)):
        left  += str(i)*int(food[i]/2)
    right = left[::-1]
    # print(left,right)
    return left+'0'+right