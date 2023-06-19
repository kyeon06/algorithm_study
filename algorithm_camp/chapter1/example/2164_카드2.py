# 카드2 문제, 큐 활용
# https://www.acmicpc.net/problem/2164

from collections import deque

# q = deque( _ for _ in range(1, int(input())+1) )
q = deque(range(1, int(input())+1))

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])
#print(q.popleft())
