from collections import deque

def solution(n):
    dq = deque(str(n))
    
    result = 0
    for i in dq:
        result += int(i)
    
    return result