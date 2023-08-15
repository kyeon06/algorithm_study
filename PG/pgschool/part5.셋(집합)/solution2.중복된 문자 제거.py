def solution(my_string):
    answer = ''
    chk = {}
    
    for st in my_string:
        if st not in chk:
            chk[st] = 0
            answer += st
        
    return answer