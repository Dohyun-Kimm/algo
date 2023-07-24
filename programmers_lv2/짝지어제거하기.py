def solution(s):
    stack = []
    for c in s:
        if stack:
            if c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    if stack:
        return 0
    else:
        return 1

# 문제 설명
# 주어진 문자열에서 같은 문자가 두번 연속으로 나오면 제거하기.
# 제거를 반복해서 문자열의 모든 문자를 제거 할 수있다면 1반환
# 그렇지 않다면 0 반환

# 문제풀이.
# stack 배열을 만들고 주어진 문자열을 하나씩 stack에넣기
# 넣기 전에 stack의 마지막 문자와 비교해서 넣으려는 문자가 stack의 마지막 문자와 같으면 제거
# 위 과정을 문자열끝까지 반복
# 반복이 끝났을때 stack에 문자가 남아있다면 return 0
# 스택이 비었다면 모두 지워진 것으로 return 1