def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    ty, tm, td = map(int, today.split('.'))
    today_to_date = ty * 12 * 28 + tm * 28 + td

    for term in terms:
        t_type, t_len = term.split(' ')
        term_dict[t_type] = int(t_len)

    for idx, privacy in enumerate(privacies):
        contract_date, contract_type = privacy.split(' ')
        yyyy, mm, dd = map(int, contract_date.split('.'))

        mm += term_dict[contract_type]
        contract_date = yyyy * 12 * 28 + mm * 28 + dd
        if contract_date <= today_to_date:
            answer.append(idx + 1)

    return answer