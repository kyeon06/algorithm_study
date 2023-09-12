# 옹알이(1)

def solution(babbling):
    
    cnt = 0
    for ba in babbling:
        
        ba = ba.replace('aya', '1')
        ba = ba.replace('ye', '1')
        ba = ba.replace('woo', '1')
        ba = ba.replace('ma', '1')
        ba = ba.replace('1', '')
    
        if len(ba) == 0:
            cnt += 1
            
    return cnt

