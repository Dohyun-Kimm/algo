# 후기
# 처음에 어떻게 접근할지 생각이 나지 않아서 1부터 12까지 경우의 수를 쭉 따졌다.
# 그리고 거리별 최적의 경로에 대한 규칙을 찾았고 이것을 구현할 방법을 생각했다.
# n이 홀수 일때는 무조건 +1만큼 가기 위해 에너지를 소모 해야하고
# 짝수일때는 순간이동을 하면 되기때문에 에너지 소모가 없었다.
# 거리가 10억까지 가능하기 때문에 계산을 최대한 적게 해야할것 같았고,
# 배열에 모든 케이스를 저장하면 메모리는 많이 써도 계산을 굳이 할 필요 없다고 생각했지만,
# 각 테스트케이스마다 계산을 해야하므로 의미 없는 일이었다.
# 모든 경우의 수를 배열에 담는 방법 보다 계산 자체를 적게할 방법이 있었다.
# 생각 하다보니 재귀로 풀수 있을것 같았고,  생각한 시간에 비해 풀이는 정말 짧았다.
#
#

# binary problem
# 2: +1, * -> 1
# 3: + 1, * +1 -> 2
# 4: +1, *, * => 1
# 5: +1, *, *, +1 -> 2
# 6: +1, *, +1,* -> 2
# 7: +1, *, +1, *, +1 -> 3
# 8: +1, *, *, * -> 1
# 9: +1, *, *,*, +1 ->2
# 10: +1, *, *, +1, * -> 2
# 11: +1, *, +1,
# 12 : +1, *, +1, *, * => 12

# 내 풀이
def solution(n):

    def foo(s):
        if s < 3:
            return 1
        else:
            if s % 2:
                return foo((s - 1) // 2) + 1
            else:
                return foo(s // 2)

    ans = foo(n)
    return ans

## 다른사람의 풀이
# def solution(n):
#     return bin(n).count('1')

## 시간 초과 풀이
# table = [0,1,1] + [0 for _ in range(3,10**9+1)]
    # LIMIT = 1000000000
    # for  i in range(3,n+1):
    #     if i % 2:
    #         table[i]= table[(i-1)//2] + 1
    #     else:
    #         table[i]= table[i//2]