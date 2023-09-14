def solution(number, k):
    stack = []
    cnt = 0
    for n in number:
        if not stack:
            stack.append(n)
        else:
            while cnt < k and stack and stack[-1] < n:
                stack.pop()
                cnt += 1
            # print('?',stack[-1], n, stack[-1]<n)
            stack.append(n)

    # print(stack,cnt)
    return ''.join(stack[:len(number) - k])



##
'''
 문제를 파악하는데 시간을 더 쓰는 연습을 해야겠다
 요즘 들어 문제 풀이가 하나도 생각나질 않는다....
 스택을 사용해서 풀어야겠다느 생각 까지는 했지만 그 과정을 구체적으로 
 그려내지를 못했다. 구체적인 시뮬레이션이 잘 안된다.
 
'''