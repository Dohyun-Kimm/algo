# 2023 4 10
# 1182 부분 수열의 합.

#  정수 수열 길이:N
# 수열의 원소의 합이 S 경우의 수

# 접근 방식 : 조합. 길이가 1인 조합, ~ 길이가 N인 조합.
# -7, -3, -2, 5, 8, (-7,-3),

# 조합의 합이 S 가 될때  count +1 
# 중복 없는 순열
# permu (부분 수열의 길이, 시작 인덱스, ,부분 수열 결과값)

N, S = map(int, input().split())
arr = list(map(int,input().split()))
count =0
def permu(n,start,P):
    # print(P)
    global S,count
    if len(P) !=0:
        if sum(P) == S:
            count +=1
    if len(P) == n:
        return
    for i in range(start,n):
        permu(n,i+1,P + [arr[i]])


permu(N,0,[])
print(count)