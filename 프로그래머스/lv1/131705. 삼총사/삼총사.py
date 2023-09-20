from itertools import combinations

def solution(number):
    answer = 0
    
    for i in combinations(number,3):
        if i[0] + i [1] + i[2] == 0:
            answer += 1
    
    
    return answer