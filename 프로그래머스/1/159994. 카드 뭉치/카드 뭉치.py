def solution(cards1, cards2, goal):
    answer = ""
    chk = "".join(goal)
    
    for g in goal:
        if g in cards1:
            answer += cards1.pop(0)
        elif g in cards2:
            answer += cards2.pop(0)
    
    return "Yes" if answer == chk else "No"