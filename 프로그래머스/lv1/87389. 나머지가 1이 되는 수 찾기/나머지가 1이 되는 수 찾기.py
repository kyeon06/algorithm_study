def solution(n):
    num = []
    for x in range(1,n):
        if n % x == 1:
            num.append(x)
    return min(num)