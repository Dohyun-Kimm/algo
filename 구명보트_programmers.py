def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    p = 0
    while True:
        person = people.pop()
        # print(person)
        length = len(people)
        for i in range(p, length):
            if people[i] + person <= limit:
                people[i] += person
                p = i
                break
        else:
            people.append(person)
            break
    # print(people)
    return len(people)

# 사람들 내림 차순으로 정렬
# 가장 몸무게가 낮은 사람을 pop받아서
# 배열 맨 앞에서 부터 대입 해줌
# 더해서 limit 보다작거나 같으면 더해줌
# 크면 다음 값으로 이동
# 맨마지막에 어디에도 넣을수 없기때문에 다시 배열에 추가.

