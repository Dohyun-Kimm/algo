def solution(strings, n):
    answer = []
    strings.sort()
    answer = sorted(strings, key=lambda x: x[n])
    #     str_dict = {}
    #     for string in strings:
    #         str_dict[string[n:]] = string[:n]
    #     sorted_dict = sorted(str_dict.items())
    #     # print(sorted_dict)
    #     for tup in sorted_dict:
    #         answer.append(  ''.join(tup[1] + tup[0]))

    return answer



## 다시 풀기