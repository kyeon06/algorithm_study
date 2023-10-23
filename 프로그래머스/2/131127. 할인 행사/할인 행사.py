def solution(want, number, discount):
    answer = 0
    want_dict = { k:v for k,v in zip(want,number)}
    
    for d in range(len(discount)-9):
        chk_count = 0
        discount_10 = discount[d:d+10]
        for w in want:
            if want_dict[w] == discount_10.count(w):
                chk_count += 1
        
        if chk_count == len(want):
            answer += 1
        
        chk_count = 0

    return answer