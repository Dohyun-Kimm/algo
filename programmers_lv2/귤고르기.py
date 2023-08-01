def solution(k, tangerine):
    answer = 0
    tang_dict = dict()
    for t in tangerine:
        if t not in tang_dict:
            tang_dict[t] = 1
        else:
            tang_dict[t] += 1
    # print(tang_dict)
    sorted_tang = dict(sorted(tang_dict.items(), key=lambda x: x[1], reverse=True))
    # print(sorted_tang)
    for key, value in sorted_tang.items():
        if k - value > 0:
            k -= value
            answer += 1
        else:
            answer += 1
            break

    return answer

# 문제 풀이
# 구해야하는 것을 파악하는데 시간이 좀 걸렸다.
# 가능한 적은 종류로, 박스에 귤을 채우는 것이라고 나와있지만,
# 가장 빈도 높은 순으로 귤을 박스에 채우면 되는 것과 같은 말이다.
# 귤의 크기 종류가 1~ 1억이기 때문에 반복문을 최소화 해야했다.
# tangerine 배열의 길이는 최대가 1천이라 반복문을 돌려도 된다고 판단했다.
# 귤의 사이즈와 개수를 한번에 저장하기 위해 딕셔너리를 선언하고
# 귤 사이즈를 키, 개수를 값으로 넣고 딕셔너리를 채웠다.
# 지금생각해보니 tang_dict[t] = tangerine.count(t)
# 이렇게하고 한번도 카운트 안한 귤 사이즈만 계산해주면 더 간단한 코드가 나오지 않았을까 싶다.
# 아무튼 딕셔너리를 채운뒤, value를 기준으로 내림차순 정렬을 해주었다.
# 사이즈의 빈도가 높은것이 앞으로 오게 해야 계산이 편할것 같았다.
# 한상자에 k개가 들어가기 때문에 딕셔너리 벨류 값을 k에서 빼주었다.
# k가 0보다 같거나 작은 시점에 계산을 끝내면 된다.


## 굳이 딕셔너리 쓸필요도 없었다.
#  사이즈를 저장하는 배열 하나, 카운트개수를 저장하는 배열하나 선언해할수도 있었다.
# 람다를 사용한 정렬 연습했다고 생각하기로 했따.