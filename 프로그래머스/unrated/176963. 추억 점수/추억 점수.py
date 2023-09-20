def solution(name, yearning, photo):
    answer = []
    
    for people in photo:
        result = 0
        for p in range(len(people)):
            if people[p] in name:
                result += yearning[name.index(people[p])]
        answer.append(result)
    return answer