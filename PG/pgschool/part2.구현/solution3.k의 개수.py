def solution(i, j, k):
    answer = ''
    for v in range(i, j+1):
        answer += str(v)
    
    cnt = 0
    for s in list(answer):
        if s == str(k):
            cnt += 1

    return cnt

print(solution(1,13,1))