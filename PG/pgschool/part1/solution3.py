# OX 퀴즈

def solution(quiz):
    quiz_list = []
    for q in quiz:
        quiz_list.append(q.split(" = "))
    
    result = []
    for qz in quiz_list:
        if eval(qz[0]) == int(qz[1]):
            result.append("O")
        else:
            result.append("X")

    return result