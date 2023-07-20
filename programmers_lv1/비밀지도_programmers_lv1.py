## 다시풀기
def solution(n, arr1, arr2):
    mmap = []
    for idx, (r1, r2) in enumerate(zip(arr1, arr2)):
        map1 = bin(r1)[2:]  # 0b#### 이런식
        map2 = bin(r2)[2:]
        if len(map1) < n:
            nn = n - len(map1)
            map1 = '0' * nn + map1
        if len(map2) < n:
            nn = n - len(map2)
            map2 = '0' * nn + map2

        secret_row = ''
        for i in range(n):
            print(map1[i], map2[i])
            if map1[i] == '0' and map2[i] == '0':
                secret_row += ' '
            else:
                secret_row += '#'
        mmap.append(secret_row)

    return mmap

#
# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer