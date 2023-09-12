def solution(numbers):
    numList = [_ for _ in range(10)]
    
    result = 0
    for num in numList:
        if num not in numbers:
            result += num

    return result