def solution(strings, n):
    guide = [[s[n], s] for s in strings]
    guide = sorted(guide)
    result = [guide[s][1] for s in range(len(strings))]
    return result