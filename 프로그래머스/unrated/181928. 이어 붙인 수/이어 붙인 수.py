def solution(num_list):
    answer = 0
    
    a = [str(i) for i in num_list if i % 2 == 0]
    b = [str(j) for j in num_list if j % 2 == 1]
    
    answer = int("".join(a)) + int("".join(b)) 
    return answer