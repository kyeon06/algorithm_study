# 스택을 이용하는 문제
# https://www.acmicpc.net/problem/9012

for _ in range(int(input())):

    # stack 생성
    st = []

    # 결과 출력을 위한 bool
    isVPS = True

    for v in input(): 
        if v == '(':
            st.append(v)
        else:
            if st:
                st.pop()
            else:
                isVPS = False
                break

    if st:
        isVPS = False

    print('YES' if isVPS else 'No')





