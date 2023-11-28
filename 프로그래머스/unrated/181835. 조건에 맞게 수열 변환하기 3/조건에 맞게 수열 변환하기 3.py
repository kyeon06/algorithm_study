def solution(arr, k):

    if k % 2 == 1:
        answer = [a * k for a in arr]
    else:
        answer = [b + k for b in arr]
    return answer