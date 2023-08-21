def solution(fees, records):
    answer = []
    # fee : [기본시간, 기본 요금, 단위시간, 단위 요금]
    # records : [시각, 차량번호, 내역]
    default_time, default_fee, unit_time, unit_fee = fees
    parking_log = dict()
    for r in records:
        time, car_num, in_out = r.split()
        if car_num in parking_log.keys():
            parking_log[car_num].append(time)
            parking_log[car_num].append(in_out)
        else:
            parking_log[car_num] = [time, in_out]

    parking_log = dict(sorted(parking_log.items()))
    # print(parking_log)
    for car in parking_log.keys():
        car_log = parking_log[car]
        in_log = []
        car_fee = 0
        parked_time = 0
        for i in range(0, len(car_log), 2):
            if car_log[i + 1] == 'IN':
                in_log.append(car_log[i])
            else:
                in_time = in_log.pop()
                out_time = car_log[i]

                # 시간 계산 변환
                out_H, out_min = map(int, out_time.split(':'))
                out_min += out_H * 60
                in_H, in_min = map(int, in_time.split(':'))
                in_min += in_H * 60
                parked_time += out_min - in_min
                # print(car,parked_time)
        if in_log:
            last_in = in_log.pop()
            last_H, last_min = map(int, last_in.split(':'))
            last_min += last_H * 60
            midnight = 24 * 60 - 1
            parked_time += midnight - last_min
        #  요금 계산
        if parked_time > default_time:
            car_fee += default_fee + int((parked_time - default_time) / unit_time) * unit_fee
            if (parked_time - default_time) % unit_time:
                car_fee += unit_fee
        else:
            car_fee = default_fee
        answer.append(car_fee)

    return answer

# 문제 풀이
# 주어진 데이터를 조작해야할 필요가 있었다.
# 헷갈리지 않기 위해 변수를 많이 선언했다.
# 요금 계산을 하는 과정에서 코드가 복잡해질 수 있는 것 같다.
# 요금 계산하는 함수를 선언 해서 풀었으면 보기 간결했을것 같다.
# 문제를 꼼꼼하게 읽지 않아서 풀이 시간이 오래 걸렸다.