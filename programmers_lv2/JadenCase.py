def solution(s):
    answer = ''
    words = s.split(" ")    
    for idx, word in enumerate(words):
        words[idx] = word[:1].upper() + word[1:].lower()
        # words[idx] = word[0].upper() + word[1:].lower()        
    return ' '.join(words)

# 5번째줄 6번째줄 차이를 모르겠음....... 알면 추가하기

