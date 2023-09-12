def solution(arr, divisor):
    result = [n for n in arr if n%divisor == 0]

    if len(result) == 0:
        result.append(-1)
    else:
        result = sorted(result)
    
    return result