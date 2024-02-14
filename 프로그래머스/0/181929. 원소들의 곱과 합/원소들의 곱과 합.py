def solution(num_list):
    answer = 0
    
    c1 = sum(num_list)**2
    c2 = 1
    for num in num_list: c2 *= num
    
    if c1 > c2: answer = 1
    
    return answer