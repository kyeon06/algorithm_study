def solution(a, b):
    answer1 = int(str(a) + str(b))
    answer2 = int(str(b) + str(a))
    return max(answer1, answer2)