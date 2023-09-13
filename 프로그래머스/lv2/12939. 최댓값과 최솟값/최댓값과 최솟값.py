def solution(s):
    s_lst = [int(n) for n in s.split()]
    
    return str(min(s_lst)) + " " + str(max(s_lst))