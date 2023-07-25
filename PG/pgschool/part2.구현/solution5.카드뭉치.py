# 카드뭉치

def solution(cards1, cards2, goal):
    chk = ''.join(goal)
    result = []
    while len(goal) > 0:
        word = goal.pop(0)

        if word in cards1:
            result.append(cards1.pop(0))
        elif word in cards2:
            result.append(cards2.pop(0))

    if ''.join(result) == chk:
        return "Yes"
    else:
        return "No"

print(solution(['i','drink', 'water'], ['want', 'to'], ['i', 'want', 'to', 'drink', 'water']))
print(solution(['i', 'water', 'drink'], ['want', 'to'], ['i', 'want', 'to', 'drink', 'water']))