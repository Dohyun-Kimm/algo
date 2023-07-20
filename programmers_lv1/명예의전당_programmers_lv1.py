def solution(k, score):
    chart = []
    min_score = 100
    ans = []
    for s in score:
        chart.append(s)
        chart.sort(reverse=True)
        if len(chart) > k:
            chart.pop()
        ans.append(chart[-1])

    # ans.sort()
    return ans