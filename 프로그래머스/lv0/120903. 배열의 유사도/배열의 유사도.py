def solution(s1, s2):
    cnt = 0
    for s in s1:
        if s in s2:
            cnt += 1
    return cnt