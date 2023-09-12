from itertools import combinations_with_replacement
# 라이언이 이길 수 있는 방법을 제시하자

def solution(n,info):
    gap_score = 0
    result = [-1]
    for i in list(combinations_with_replacement(range(0,11), n)):
        ryan_info = [0] * 11
        for score in i:
            ryan_info[10-score] += 1

        apeach_score, ryan_score = 0, 0
        for i in range(11):
            if (info[i], ryan_info[i]) == (0,0):
                continue    
            elif ryan_info[i] > info[i]:
                ryan_score += 10-i
            else:
                apeach_score += 10-i
        gap = ryan_score - apeach_score

        if gap_score < gap:
            gap_score = gap
            result = ryan_info

    return result