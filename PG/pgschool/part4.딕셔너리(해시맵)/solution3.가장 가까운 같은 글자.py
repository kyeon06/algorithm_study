# 가장 가까운 같은 글자
# https://school.programmers.co.kr/tryouts/85914/challenges?language=python3

def solution(s):
    check = {}
    answer = []
    for idx, c in enumerate(s):
        if c in check:
            answer.append(idx - check[c])
            check[c] = idx
        else:
            answer.append(-1)
            check[c] = idx
    return answer