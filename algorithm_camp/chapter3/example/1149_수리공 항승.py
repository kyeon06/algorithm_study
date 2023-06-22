# 수리공 항승
# https://www.acmicpc.net/problem/1449

N, L = map(int, input().split())
coord = [False] * 1001

for i in map(int, input().split()):
    coord[i] = True

x = 0
cnt = 0
while x < 1001:
    if coord[x]:
        cnt += 1
        x += L
    else:
        x += 1

print(cnt)
