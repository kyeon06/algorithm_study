"""
[문제]
자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.
"""

def solution(n):
    num = []
    for x in range(1,n):
        if n % x == 1:
            num.append(x)
    
    return min(num) # 굳이 min을 하지 않고 num[0] 꺼내면 됨


# 간단하게 바꿔보기
def solutionB(n):
    return [x for x in range(1,n) if n % x == 1][0]

# Test
print(solution(10))
print(solutionB(10))
