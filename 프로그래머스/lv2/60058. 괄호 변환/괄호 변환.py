# 올바른 괄호 문자열인지 아닌지 판단하는 함수
def ischeck(p):
    # 빈 리스트 생성
    vps_list = []
    for x in p:
        if x == "(":
            vps_list.append(x)
        elif x == ")":
            if len(vps_list) > 0:
                vps_list.pop()
            else:
                vps_list.append(x)
                break

    if len(vps_list) == 0:
        result = True
    else:
        result = False

    return result

# 균형잡힌 문자열인지 판단하는 함수
def isbalance(u):
    k = 0
    for c in u:
        if c == "(":
            k +=1
        elif c == ")":
            k -=1
    
    if k == 0:
        return True
    else:
        return False

# 올바른 괄호 문자열로 반환
def solution(w):
    if w == "" or ischeck(w) == True:
        return w

    for i in range(2, len(w)+1, 2):
        u = w[0:i]
        v = w[i:]

        # u가 균형이 잡혀있는지 아닌지 확인
        if isbalance(u) == True:
            if ischeck(u) == True:
                return u + solution(v)
            else:
                s = "(" + solution(v) + ")" #4-1,2,3
                for j in u[1:-1]: #4-4
                    if j == "(":
                        s += ")"
                    else:
                        s += "("
            return s