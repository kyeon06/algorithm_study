def solution(s):

    st = []
    for i in s:
        if len(st) == 0:
            st.append(i)
        else:
            if st[-1] == i:
                st.append(i)
            else:
                if st[-1] == "(":
                    st.pop()
                else: st.append(i)
    
    if len(st) == 0:
        return True
    
    return False