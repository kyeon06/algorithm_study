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


# 다른 풀이
def solution1(lottos, win_nums):
    cnt_corr = 0 # 당첨 가능한 최저 개수
    cnt_zero = 0 # 알아볼 수 없는 번호
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt_corr += 1
        if lottos[i] == 0:
            cnt_zero += 1
            
    total = cnt_corr + cnt_zero # 당첨 가능한 최고 개수

    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6} # 순위와 당첨 내용 딕셔너리
 
    answer = [rank[total],rank[cnt_corr]]
    
    return answer

def solution2(lottos, win_nums):
    answer = [0,0]
    rank = [6,6,5,4,3,2,1]

    cnt = 0
    cntz = lottos.count(0) # 0개수 저장

    for v in lottos:
        if v in win_nums:
            cnt += 1
    
    answer[0], answer[1] = rank[cnt+cntz], rank[cnt]

    return answer