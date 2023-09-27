def solution(money):
    
    cnt = money // 5500
    result = money - (5500 * cnt)
    return [cnt, result]