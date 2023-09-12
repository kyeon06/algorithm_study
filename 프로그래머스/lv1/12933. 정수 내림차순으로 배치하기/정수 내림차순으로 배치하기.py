def solution(n):
    num = [s for s in str(n)]
    return int(''.join(sorted(num, reverse=True)))