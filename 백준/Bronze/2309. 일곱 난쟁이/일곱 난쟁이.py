from itertools import combinations

# 제출 했을 때 "틀렸습니다..."
# 가능한 정답이 여러가지 인 경우 아무거나 출력한다 => 아래의 코드는 모든 경우에 대한 출력을 하게 된다.
heights = [int(input()) for _ in range(9)]

for i in combinations(heights, 7):
    if sum(i) == 100:
        for height in sorted(i):
            print(height)
        
        break