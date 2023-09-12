# 369게임

def solution(order):
    answer = 0
    for v in list(str(order)):
        if v == '3' or v == '6' or v == '9':
            answer += 1

    return answer