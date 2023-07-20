def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        count = 0
        j =1
        while j <=int(i**(1/2)):
            if i % j ==0:
                count +=1
                if j ** 2 !=i:
                    count +=1
            j+=1
        if count <= limit:
            answer += count
        else:
            answer += power
    return answer
## 다른풀이
# def cf(n): # 공약수 출력
#     a = []
#     for i in range(1,int(n**0.5)+1):
#         if n%i == 0:
#             a.append(n//i)
#             a.append(i)
#     return len(set(a))
# def solution(number, limit, power):
#     return sum([cf(i) if cf(i)<=limit else power for i in range(1,number+1)])