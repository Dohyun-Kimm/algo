def solution(sequence, k):
    start = 0
    end = 0
    n = len(sequence)
    leng = 99999999
    cnt = sequence[0]
    answer = []

    while True:
        if cnt == k:
            if end - start + 1 < leng:
                leng = end - start + 1
                answer = [start, end]
                if end < n - 1:
                    end += 1
                    cnt += sequence[end]
                else:
                    if start < n - 1:
                        cnt -= sequence[start]
                        start += 1
                    else:
                        break
            else:
                if end < n - 1:
                    end += 1
                    cnt += sequence[end]
                else:
                    if start < n - 1:
                        cnt -= sequence[start]
                        start += 1
                    else:
                        break
        elif cnt < k:
            if end < n - 1:
                end += 1
                cnt += sequence[end]
            else:
                break
        elif cnt > k:
            if start < n - 1:
                cnt -= sequence[start]
                start += 1
            else:
                break


    return answer