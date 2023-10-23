def least(a,b):
    A,B = a,b
    
    while b > 0:
        a, b = b, a % b
    
    gcd = a
    return A * B // gcd

def solution(arr):
    arr.sort()
    answer = arr[0]
    
    for i in range(1, len(arr)):
        answer = least(answer, arr[i])
    
    return answer