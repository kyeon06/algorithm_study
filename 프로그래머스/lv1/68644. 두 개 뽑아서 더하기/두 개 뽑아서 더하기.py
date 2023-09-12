def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            tmp = numbers[i] + numbers[j]
            if tmp in result:
                continue
            else:
                result.append(tmp)
    return sorted(result)