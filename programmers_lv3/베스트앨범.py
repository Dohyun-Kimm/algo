# 1트 실패
# def solution(genres, plays):
#     answer = []
#     stats = dict()
#     # played = [ (i,genres[i],plays[i]) for i in range(len(genres))]
#     for i in range(len(genres)):
#         if genres[i] not in stats.keys():
#             stats[genres[i]] = [[i, plays[i]]]
#         else:
#             stats[genres[i]].append([i, plays[i]])
#     for val in stats.values():
#         val.sort(key=lambda x: x[1], reverse=True)
#     print(stats)
#     # 장르별 순위
#     genre_type = list(set(genres))
#     genre_rank = dict()
#     for i in range(len(genre_type)):
#         genre_rank[genre_type[i]] = 0
#     for i in range(len(genres)):
#         genre_rank[genres[i]] += plays[i]
#     tmp = sorted(genre_rank.items(), key=lambda x: x[1], reverse=True)
#     print(tmp)
#
#     return answer
# 2nd 성공
def solution(genres, plays):
    answer = []
    stats = dict()
    # played = [ (i,genres[i],plays[i]) for i in range(len(genres))]
    for i in range(len(genres)):
        if genres[i] not in stats.keys():
            stats[genres[i]] = [[i, plays[i]]]
        else:
            stats[genres[i]].append([i, plays[i]])
    for key, val in stats.items():
        val.sort(key=lambda x: x[1], reverse=True)
        stats[key] = val[:2]
    # print(stats)
    # 장르별 순위
    genre_type = list(set(genres))
    genre_rank = dict()
    for i in range(len(genre_type)):
        genre_rank[genre_type[i]] = 0
    for i in range(len(genres)):
        genre_rank[genres[i]] += plays[i]
    tmp = sorted(genre_rank.items(), key=lambda x: x[1], reverse=True)
    # print(tmp)
    for k in tmp:
        g, p = k
        # print(g,p)
        # print(stats[g])
        for i, j in stats[g]:
            answer.append(i)

    return answer