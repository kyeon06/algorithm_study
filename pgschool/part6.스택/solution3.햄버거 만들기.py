def solution(ingredient):
    answer = 0
    burger = [1,2,3,1]
    st = []
    for i in ingredient:
        st.append(i)
        if st[-4:] == burger:
            del st[-4:] # pop() or del 사용해서 삭제할 것. 슬라이싱하면 시간 오래걸림
            answer += 1
        
    return answer