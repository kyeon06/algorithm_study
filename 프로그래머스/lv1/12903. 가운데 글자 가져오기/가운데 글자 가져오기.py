def solution(s):
    
    if len(s) % 2 == 0:
        result = s[len(s)//2-1: len(s)//2+1]
    else:
        result = s[len(s)//2]
    
    return result