def solution(arr1, arr2):
    answer = [[0]*len(arr1[0]) for _ in range(len(arr1))]
    # print(answer)
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            # print(arr1[i][j],arr2[i][j],i,j)
            answer[i][j] = arr1[i][j]+arr2[i][j]
            # print(answer,i,j)
    return answer


## 행렬 선언 방식 기억하기
# answer = [[0]*len(arr1[0])]*len(arr1)
# len(arr1) 개의 동일한 참조를 가진 하위 리스트로 구성됩니다.
# 이는 실제로는 각 행이 동일한 객체를 참조하므로
# 하나의 행을 수정하면 모든 행이 같은 값을 가지게 됩니다.
