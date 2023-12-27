def hanoi(num,start,end,mid,arr):
    print(num,start,end,mid,arr)
    if num == 1:
        arr.append([start,end])
        return
    else:
        hanoi(num-1,start,mid,end,arr)
        arr.append([start,end])
        hanoi(num-1,mid,end,start,arr)

def solution(n):
    answer = []
    # 첫 동작을 수행한 결과.
    hanoi(n,1,3,2,answer)
    return answer
'''
    문제 이해 잘못함. 
    원판을 옮긴뒤의 어느 탑에 원판이 있는지를 answer에 추가하는 것이 아니라
    어느 원판에서 어느 원판으로 옮겼는지를 추가하는것.
'''
print(solution(2))