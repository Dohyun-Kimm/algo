def solution(orders, course):
    answer = []
    menus = dict()

    def combi(name, length, order_len):
        if len(name) == length:
            if name not in menus:
                menus[name] = 1
            else:
                menus[name] += 1
            return
        for i in range(len(orders[order_len])):
            if checked[i] == 0:
                checked[i] = 1
                combi(name + orders[order_len][i], length, order_len)

    # 모든 orders 원소들에 대해서
    for idx, order in enumerate(orders):
        for c in course:
            checked = [0 for _ in range(len(order))]  # 중복방지용 배열
            combi('', c, idx)
    print(menus)
    ans = sorted(menus.items(), key=lambda x: x[1], reverse=True)
    print(ans)
    j = 0
    for el in range(ans):
        if not answer:
            answer.append(el[0])
            cnt = el[1]
            unit_len = len(el[0])
        else:
            if el[1] ==

    return answer


'''
모든 대문자로 조합 만들면 경우가 너무 많아지므로
각 원소들에 대해서 course 에 들어잇는 원소의 개수조합 만들기
조합이 있으면 cnt +1 하고 없으면 딕셔너리에 추가하기.
조합을 뽑아 내는 과정에있어서 문제각 좀 생겼는데 파악을 못하겠다.
'''

# 다른 사람의 풀이
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]