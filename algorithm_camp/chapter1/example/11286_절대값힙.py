# 절대값 힙 문제
# https://www.acmicpc.net/problem/11286

import heapq
import sys

# 빠른 입출력을 위함, 파이썬 같은 경우 10만개의 데이터를 돌릴 때 시간이 오래 걸림
input = sys.stdin.readline

pq = []
for _ in range(int(input())):
    x = int(input())

    if x:
        # 원본값과 절대값을 튜플 형식으로 같이 저장(나중 비교를 위함)
        heapq.heappush(pq, (abs(x), x))
    else:
        print(heapq.heappop(pq)[1] if pq else 0)