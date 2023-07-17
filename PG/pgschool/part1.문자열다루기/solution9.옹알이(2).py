def solution(babbling):

    result = 0
    for b in babbling:
        b = b.replace("aya", '1')
        b = b.replace("ye", '1')
        b = b.replace("woo",'1')
        b = b.replace("ma", '1')
        b = b.replace('1', '')

        print(b)
        if len(b) == 0:
            result += 1
    
    return result

# 연속적인 부분을 해결하지 못함
# 아래 해결 방법


def solution(babbling):

    words = ["aya", "ye", "woo", "ma"]

    result = 0
    for b in babbling:

        for w in words:
            if w*2 not in b:
                b = b.replace(w, '1')
        
        b = b.replace('1', '')
        if len(b) == 0:
            result += 1
    
    return result