def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        # skill_trees에서 하나씩 뽑아 skill에 있는 알파벳을 하나(s)로 만든다
        s = ""
        for sk in skill_tree:
            if sk in skill:
                s += sk
        # skill에서 s의 길이만큼 잘라 s랑 비교한 후 같으면 answer + 1
        if skill[:len(s)] == s:
            answer += 1
    return answer