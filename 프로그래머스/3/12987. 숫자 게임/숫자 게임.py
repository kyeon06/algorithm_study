def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    for sA in A:
        if sA < B[0]:
            answer += 1
            del B[0]
    return answer