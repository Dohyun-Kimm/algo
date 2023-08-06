

def solution(arr1, arr2):
    answer  = [[0 for _ in range(len(arr2[0]))]for _ in range(len(arr1))]
    print(*arr2)
    # anwer[i][j] = sum(arr1[i][j]* arr2[j][i])
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer

# 다른 사람의 풀이
# def productMatrix(A, B):
#     return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
# sum(a * b for a,b, in zip(A_row, B_col)) for B_col in zip(*B)
# zip(*B)이 행렬의 transpose의 효과를 가져옴. unpacking한 뒤 zip