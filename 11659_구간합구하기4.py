#11659 구간 합 구하기

import sys
input = sys.stdin.readline

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# sum_arr = [arr[0]] + [0 for _ in range(N-1)]
# for i in range(1,N):
#     sum_arr[i] = sum_arr[i-1] + arr[i]
# # print(sum_arr)
#
# for j in range(M):
#     start, end = map(int,input().split())
#     if start == 1:
#         print(sum_arr[end - 1])
#     else:
#         print(sum_arr[end-1]-sum_arr[start-2])

################
N, M = map(int, input().split())
nums = list(map(int, input().split()))

# accumulated_sum = [nums[0]] + [0] * (N-1)
#
for i in range(1, N):
    nums[i] = nums[i-1] + nums[i]

for i in range(M):
    s, l = map(int, input().split())
    s, l = s-1, l-1
    if s == 0:
        print(nums[l])
    else:
        print(nums[l] - nums[s-1])