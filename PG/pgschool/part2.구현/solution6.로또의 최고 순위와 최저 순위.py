def solution(lottos, win_nums):
    
    zero_cnt = 0
    for z in lottos:
        if z == 0:
            zero_cnt += 1

    if zero_cnt == 6: return [1, 6]

    cnt = 0
    for v in lottos:
        if v in win_nums:
            cnt += 1

    if cnt == 6:
        return [1, 1]
    elif cnt == 5:
        return [1, 2]
    elif cnt == 4:
        return [ 3-zero_cnt , 3]
    elif cnt == 3:
        return [ 4-zero_cnt ,4]
    elif cnt == 2:
        return [ 5-zero_cnt, 5]
    else:
        return [ 6-zero_cnt , 6]