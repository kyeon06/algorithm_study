# def solution(n):

#     num = [0,1]
#     for i in range(n):
#         num.append(num[i] + num[i+1])

#     return num[n] % 1234567

def solution(num):
    
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
        
    return a % 1234567