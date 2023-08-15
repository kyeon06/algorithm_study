def solution(s):
    answer = True
    
    st = []
    
    for i in s:
        st.append(i)
        if st[-2:] == ["(",")"]:
            del st[-2:]
        
    if len(st) > 0:
        return False

    return True