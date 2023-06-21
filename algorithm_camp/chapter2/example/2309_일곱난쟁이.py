# 일곱난쟁이 / 브루트포스
# https://www.acmicpc.net/problem/2309

from itertools import combinations

heights = [int(input()) for _ in range(9)]

for i in combinations(heights, 7):
    if sum(i) == 100:
        for height in sorted(i):
            print(height)