def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx, h in enumerate(citations):
        if idx >= h:
            return idx
    return len(citations)
#     max_h = citations[0]
#     idx = 0
#     while idx < len(citations):

#         if citations[idx] < max_h:
#             if idx>= max_h and len(citations)-(idx) <= max_h:
#                 print(citations[idx],idx, len(citations)-idx)
#                 return idx
#             else:
#                 if citations[idx+1] <max_h:
#                     max_h -= 1
#                 # idx = 0
#         else:
#             idx += 1




## 문제를 이해하는데 오래걸렸다.
# 어렵게이해한만큼생각이 꼬여서 풀이가 이상해졌었다.