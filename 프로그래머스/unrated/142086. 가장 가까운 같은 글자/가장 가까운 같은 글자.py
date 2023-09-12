def solution(s):
    lst = []
    result = []
    for w in range(len(s)):
        if s[w] in lst:
            result.append(w - "".join(lst).rindex(s[w]))
            lst.append(s[w])
        else:
            result.append(-1)
            lst.append(s[w])
    
    return result