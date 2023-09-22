def solution(n):

    num = [0,1]
    for i in range(n):
        num.append(num[i] + num[i+1])

    return num[n] % 1234567