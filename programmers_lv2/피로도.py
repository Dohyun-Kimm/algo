def solution(k, dungeons):
    answer = 0
    cnt = 0
    checked = [0 for i in range(len(dungeons))]

    def foo(energy, count):
        nonlocal answer
        if count > answer:
            answer = count

        for idx in range(len(dungeons)):
            if not checked[idx]:
                required, need = dungeons[idx]
                if energy >= required:
                    remain = energy - need
                    checked[idx] = 1
                    foo(remain, count + 1)
                    checked[idx] = 0

    foo(k, cnt)

    return answer

## 문제풀이
# 모든 경우의 수를 탐색해야하는 문제였다.
# 가지고 있는 피로도로 입장할수 있는 던전을 찾고, 던전이 요구하는 소모량을 피로도에서 빼주는 과정을
# 백트래킹으로 구현했다.
# 