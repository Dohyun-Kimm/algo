## 다시 풀기

def solution(brown, yellow):
    total = brown + yellow  # a * b = total
    for b in range(1, total + 1):
        if (total / b) % 1 == 0:  # total / b = a
            a = total / b
            if a >= b:  # a >= b
                if 2 * a + 2 * b == brown + 4:  # 2*a + 2*b = brown + 4 
                    return [a, b]

