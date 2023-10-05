def solution(k, tangerine):
    answer = 0
    chk = {}
    for t in tangerine:
        if t in chk:
            chk[t] += 1
        else:
            chk[t] = 1
    
    chk = dict(sorted(chk.items(), key=lambda x: x[1], reverse=True))
    
    for i in chk:    
        if k <= 0:
            return answer
        k -= chk[i]
        answer += 1
    
    return answer