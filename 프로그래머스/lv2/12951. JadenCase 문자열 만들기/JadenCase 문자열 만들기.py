def solution(s):
    answer = ''
    s = s.split(" ")
    for i in range(len(s)):
        if s[i] == "":
            continue
        elif s[i][0].isdigit():
            s[i] = s[i][0] + s[i][1:].lower()
        else:
            s[i] = s[i][0].upper() + s[i][1:].lower()
        
    answer = " ".join(s)
            
    return answer