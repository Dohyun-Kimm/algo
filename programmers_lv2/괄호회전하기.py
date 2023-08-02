def solution(s):
    count = 0

    def shift(ss):
        return ss[1:] + ss[0]

    def check(sss):
        temp = []
        for ch in sss:
            if not temp:
                temp.append(ch)
            elif ch == ']' and temp[-1] == '[':
                temp.pop()
            elif ch == ')' and temp[-1] == '(':
                temp.pop()
            elif ch == '}' and temp[-1] == '{':
                temp.pop()
            else:
                temp.append(ch)
        # print(temp)
        if temp:
            return 0
        else:
            return 1

    for _ in range(len(s)):
        s = shift(s)
        # print(s)
        count += check(s)

    return count

# 문제 풀이
# 주어진 문자열을 한칸씩 회전시키면서 조건을 만족하는지 일일이 확인하는 문제였다
# 그래서 회전하는 함수, 올바른 문자열인지확인하는 함수 두개를 선언했다.
# 회전하는 함수는 첫 문자를 맨끝으로 보내서 리턴하는 함수이고
# 체크하는 함수는 괄호가 올바르게 닫히는지 비교하는 함수로, 스택을 활용해서 구현했다.
# 반복문이 끝난뒤에도 스택에 괄호가 남았다면 올바른 문자열이 아니다.
# 문자열의 길이만큼(전부 확인) 반복하면, 몇개의 올바른 문자열이 나오는지 리턴하면 풀리는 문제다.


# 다른 풀이
# from collections import deque
#
# def check(s):
#     while True:
#         if "()" in s: s=s.replace("()","")
#         elif "{}" in s: s=s.replace("{}","")
#         elif "[]" in s: s=s.replace("[]","")
#         else: return False if s else True
#
# def solution(s):
#     ans = 0
#     que = deque(s)
#
#     for i in range(len(s)):
#         if check(''.join(que)): ans+=1
#         que.rotate(-1)
#     return ans
# 느낌점
#         if "()" in s: s=s.replace("()","")
# 이렇게 string method를 사용한것이 배울 점이라고 생각했다. 굳이 스택을 활용하지 않아도 되는풀이
