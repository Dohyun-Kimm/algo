def solution(m, musicinfos):
    answer = ''
    arr = []
    for music in musicinfos:
        start, end, name, melody = music.split(',')
        runtime = (int(end[:2]) * 60 + int(end[3:])) - (int(start[:2]) * 60 + int(start[3:]))
        melody_length = len(melody)
        if runtime > melody_length:
            melody = melody * (runtime // melody_length)
            melody += melody[:runtime % melody_length]
        arr.append([runtime, name, melody])
    arr.sort(key=lambda x: x[0], reverse=True)
    # print(arr)
    for mu in arr:
        pointer = 0
        r, n, mel = mu
        cnt = 0
        # print('...',n,answer,mel,m,cnt)
        for unit in mel:
            # print(unit, m[pointer],pointer)
            if cnt > 0 and unit != m[pointer]:
                cnt = 0
                pointer = 0
                break
            elif cnt == 0 and unit == m[pointer]:
                cnt += 1
                pointer += 1
            elif cnt > 0 and unit == m[pointer]:
                pointer += 1
            if cnt > 0 and pointer == len(m):
                answer = n
                break

    if answer == '':
        return None
    else:
        return answer

'''
정답 조건을 맞추는게 어렵다.....

'''