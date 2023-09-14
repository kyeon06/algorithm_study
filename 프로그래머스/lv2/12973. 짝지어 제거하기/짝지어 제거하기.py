def solution(s):
    answer = -1
    st = []
    
    for e in s:
        if e not in st:
            st.append(e)
        else:
            if st[-1] == e:
                st.pop()
            else: st.append(e)
    
    if len(st) == 0:
        return 1
    else: return 0