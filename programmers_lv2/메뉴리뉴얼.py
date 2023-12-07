def solution(orders, course):
    answer = []
    combi_list = []
    menu_list = dict()

    # 가능한 모든 메뉴의 조합을 만들고 카운팅해서 딕셔너리에 추가하는 함수
    def combi(menu, source, length, start):
        if len(menu) == length:
            menu.sort()  # 알파벳의 순서 때문에 생기는 중복을 방지
            tmp = ''.join(menu)
            if tmp not in menu_list:
                menu_list[tmp] = 1
            else:
                menu_list[tmp] += 1
            combi_list.append(menu)
            return
        for j in range(start, len(source)):
            if checked[j] == 0:
                checked[j] = 1
                combi(menu + [source[j]], source, length, j)
                checked[j] = 0

    for i in range(len(orders)):
        for c in range(len(course)):
            checked = [0] * len(orders[i])
            combi([], orders[i], course[c], 0)
    # 조합이 추가된 딕셔너리를 주문 횟수가 많은 순으로 정렬하기.
    most_ordered = sorted(menu_list.items(), key=lambda x: (x[1], x[0]), reverse=True)
    # 각 코스요리 길이에 해당하는 메뉴 뽑기.
    for l in course:
        max_occurrences = 0
        for m, c in most_ordered:
            if len(m) == l:
                if c >= 2 and c >= max_occurrences:
                    if c >= max_occurrences:
                        answer.append(m)
                        max_occurrences = c
    answer.sort()
    return answer