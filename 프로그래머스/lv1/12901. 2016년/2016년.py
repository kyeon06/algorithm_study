def solution(a, b):
    yoil = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    start = yoil.index('FRI')
    month = a
    day = b
    
    for m in range(1, month):
        if m == 1:
            end = (start + 31) % 7
        elif m == 2:
            end = (end + 29) % 7
        elif m in [3,5,7,8,10,12]:
            end = (end + 31) % 7
        elif m in [4,6,9,11]:
            end = (end + 30) % 7

    if month == 1:
        result = (start+day) % 7 - 1
        result_yoil = yoil[result]
    else:
        result = (end + day) % 7 - 1
        result_yoil = yoil[result]

    return result_yoil

