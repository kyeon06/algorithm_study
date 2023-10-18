from itertools import combinations

def check_num(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    chk = []
    for x in combinations(nums,3):
        chk.append(sum(x))
    
    for i in chk:
        if check_num(i):
            answer += 1               
    
    return answer