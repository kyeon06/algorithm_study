# 가위바위보
# https://school.programmers.co.kr/tryouts/85898/challenges

def solution(rsp):
    rsp = list(rsp)
    
    answer = ''
    for v in rsp:
        if v == '0':
            answer += '5'
        elif v == '2':
            answer += '0'
        else:
            answer += '2'

    return answer

solution("205")