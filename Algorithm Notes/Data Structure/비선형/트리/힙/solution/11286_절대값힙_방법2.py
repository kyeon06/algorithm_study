# 절대값 힙 문제
# https://www.acmicpc.net/problem/11286

# min_heap, max_heap 양수 음수 따로 저장해서 푸는 방법

import heapq
import sys

input = sys.stdin.readline
min_heap = [] # 양수들만 저장
max_heap = [] # 음수들만 저장

for _ in range(int(input())):
    x = int(input())

    if x:
        if x > 0:
            heapq.heappush(min_heap, x)
        else:
            # max_heap 적용하는 방법 => 부호를 바꿔서 저장
            heapq.heappush(max_heap, -x)
        
    else:
        if min_heap:
            if max_heap:
                # max_heap에서 요소를 꺼낼 때 부호를 바꿔서 꺼낸다
                if min_heap[0] < abs(-max_heap[0]):
                    print(heapq.heappop(min_heap))
                else:
                    print(-heapq.heappop(max_heap))
            else:
                print(heapq.heappop(min_heap))
        else:
            if max_heap:
                print(-heapq.heappop(max_heap))
            else:
                print(0)
        