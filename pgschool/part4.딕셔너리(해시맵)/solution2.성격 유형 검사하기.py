# 성격 유형 검사하기
# https://school.programmers.co.kr/tryouts/85913/challenges

def solution(survey, choices):
    # 성격유형 점수판
    c_dict = { "R" : 0, "T" : 0, "C" : 0, "F": 0, "J" : 0, "M":0, "A": 0, "N" : 0}
    score = [3,2,1,0,1,2,3]
    answer = ""
    
    for sur, num in zip(survey, choices):
        if num > 4:
            c_dict[sur[1]] += score[num-1]
        elif num < 4:
            c_dict[sur[0]] += score[num-1]
    
    # 성격유형 결과
    if c_dict["R"] >= c_dict["T"]:
        answer += "R"
    else: answer += "T"
    
    if c_dict["C"] >= c_dict["F"]:
        answer += "C"
    else: answer += "F"
    
    if c_dict["J"] >= c_dict["M"]:
        answer += "J"
    else: answer += "M"
    
    if c_dict["A"] >= c_dict["N"]:
        answer += "A"
    else: answer += "N"
        
    return answer


# 다른 사람 풀이
def solution(survey, choices):
    answer = ''
    dic= {"R" : 0,"T" : 0,"C" : 0,"F" : 0,"J" : 0,"M" : 0,"A" : 0,"N" : 0 }
    
    for s,c in zip(survey,choices):
        if c>4:     dic[s[1]] += c-4
        elif c<4:   dic[s[0]] += 4-c
    
    li = list(dic.items())
    
    for i in range(0,8,2):
        if li[i][1] < li[i+1][1]: answer += li[i+1][0]
        else:   answer += li[i][0]
        
    return answer