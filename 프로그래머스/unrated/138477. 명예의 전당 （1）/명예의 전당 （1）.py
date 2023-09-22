def solution(k, score):
    answer = []
    best = []
    
    for s in score:
        
        if len(best) >= k:
            if s < min(best):
                answer.append(min(best))
                continue
            best = sorted(best, reverse=True)
            best.pop()
                
        best.append(s)
        answer.append(min(best))
            
    return answer