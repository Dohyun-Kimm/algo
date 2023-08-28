def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        idx = 0
        valid = 1
        for s in tree:
            if s in skill:
                if s == skill[idx]:
                    idx += 1
                else:
                    valid = 0
                    break
        if valid:
            answer += 1

    return answer


# 문제 풀이
# 선행 스킬이 먼저 찍혔는지 확인 하는 코드만 짜면 되는 문제다.
# 스킬트리를 순회하면서
# 연관된 스킬이 순서대로 찍혀있는지만 확인했다.