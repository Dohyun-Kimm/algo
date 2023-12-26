#틀린 풀이
# def solution(k, d):
#     answer = 0
#     # 가능한 범위 확인하기
#     boundary = []
#     for i in range(d,-1,-1):
#         for j in range(d,-1,-1):
#             if i**2 + j **2 <= d**2:
#                 boundary.append((j,i))
#                 break
#     print(boundary)
#     # 그 밑에 있는 좌표의 수 합치기
#     check = []
#     for x,y, in boundary:
#         if x not in check:
#             for i in range(x+1):
#                 if i%k ==0 and y%k==0:
#                     answer+=1
#     return answer

# 다시 풀기
import math
def solution(k, d):
    answer = 0
    for i in range(0,d+1,k):
        point = math.floor(math.sqrt(d**2 - i**2))
        answer += point // k +1
    return answer

'''
  가능한 거리에서 한쪽 좌표를 빼면 나머지 좌표를 알 수 있다.
  위의 계산 결과가 0이 아니면 허용 범위를 벗어나기 때문에 내림(floor)해준다.
  => 계산 결과가 허용 범위 내의 최대 좌표다.
  k의 배수만 카운팅 하기 때문에 반복문에서 k의 배수만 카운팅하게 한다.
  
  범위 내 최대 좌표를 k로 나누어준 몫이 찍을 수 있는 좌표의 수를 나타내고, 0을 포함해야하기 때문에 +1 해준다.
  
'''