from collections import deque

def solution(a,b):

    dq = deque(a)
    
    cnt = 0
    for i in range(len(dq)):
        
        if ''.join(dq) == b:
            return cnt
        
        dq.appendleft(dq.pop())
        cnt += 1
                         
    return -1


a = "hello"
b = "ohell"
solution(a,b)