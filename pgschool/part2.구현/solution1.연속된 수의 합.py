# 연속된 수의 합

def solution(num, total):
    avg = total // num

    answer = []
    for i in range(avg - (num-1)//2, avg + (num+2)//2):
        answer.append(i)

    return answer

print(solution(3, 12))