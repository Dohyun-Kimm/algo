def solution(id_list, report, k):
    answer = []

    report_record = {}
    reported_count = {}
    reporter = {}
    # data set
    for ids in id_list:
        report_record[ids] = set()
        reported_count[ids] = 0
        reporter[ids] = 0

    # report process
    for r in report:
        reporting, reported = r.split(' ')
        if reporting not in report_record[reported]:
            report_record[reported].add(reporting)
            reported_count[reported] += 1

    # result
    for key, value in reported_count.items():
        if reported_count[key] > k - 1:
            for val in report_record[key]:
                reporter[val] += 1
    # print(report_record)
    # print(reporter)
    for cnt in reporter.values():
        answer.append(cnt)
    return answer