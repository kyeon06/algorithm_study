def solution(n):
    answer = 0
    
    nCnt = format(n, 'b').count("1")
    nxt = n + 1
    while True:
        nxtCnt = format(nxt, 'b').count("1")
        if nCnt == nxtCnt:
            answer = nxt
            break
        else:
            nxt += 1
    return answer