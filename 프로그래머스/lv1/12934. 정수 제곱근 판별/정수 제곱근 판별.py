def solution(n):
    num = n ** 0.5
    if num == int(num):
        return (n**0.5 + 1)**2
    else:
        return -1