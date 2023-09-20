def solution(sizes):
    answer = 0
    sizes = [sorted(s, reverse=True) for s in sizes]
    row = max([a for a, b in sizes])
    col = max([b for a, b in sizes])
    return row * col