def solution(book_time):
    end_room = []
    book_time.sort(key=lambda x: x[0])
    # print(book_time)
    reservations = []
    for time in book_time:
        start, end = time
        hour_s, minuite_s = map(int, start.split(':'))
        hour_e, minuite_e = map(int, end.split(':'))
        new_start = hour_s * 60 + minuite_s
        new_end = hour_e * 60 + minuite_e + 10
        reservations.append([new_start, new_end])
    # print(reservations)
    for booking in reservations:
        start, end = booking
        if not end_room:
            end_room.append(end)
        else:
            full = True
            for i in range(len(end_room)):
                if end_room[i] <= start:
                    full = False
                    end_room[i] = end

                    break
            if full:
                end_room.append(end)

    return len(end_room)