def solution(d, budget):
    answer = 0
    
    for m in sorted(d):
        if budget >= m:
            budget -= m
            answer += 1
    return answer