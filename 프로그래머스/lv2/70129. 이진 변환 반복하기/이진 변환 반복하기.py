def solution(s):
    cnt = 0
    repeat = 0
    while True:
        repeat += 1
        for i in range(len(s)):
            if s[i] == "0":
                cnt += 1
        
        s = s.replace("0", "")
        
        if len(s) == 1:
            break
        else:
            s = bin(len(s))[2:]

    return [repeat, cnt]