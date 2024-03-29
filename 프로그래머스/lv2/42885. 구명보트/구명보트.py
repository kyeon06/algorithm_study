from collections import deque

def solution(people, limit):
    answer = 0
    
    people = deque(sorted(people, reverse=True))
    
    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            answer += 1
            people.popleft()
            people.pop()
        else:
            answer += 1
            people.popleft()
        
        if len(people) == 1:
            answer += 1
    return answer