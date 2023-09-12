def solution(absolutes, signs):
    result = 0
    for sign, num in zip(signs, absolutes):
        
        if sign:
            result += num
        else:
            result -= num

    return result
