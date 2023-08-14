# 의상

def solution(clothes):
    answer = 1

    clothesDict = {t : 0 for n,t in clothes}
    
    for n, t in clothes:
        clothesDict[t] += 1

    for t in clothesDict:
        answer *= (clothesDict[t] + 1)
    
    return answer - 1