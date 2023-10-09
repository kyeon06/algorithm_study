def solution(n):
    if n < 3:
        return n
    
    chk = [0] * (n+1)
    
    chk[1] = 1
    chk[2] = 2    
    for i in range(3, n+1):
        chk[i] = chk[i-1] + chk[i-2]
    
    return chk[n] % 1234567
