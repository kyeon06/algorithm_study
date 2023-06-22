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

# 만약 좌표 범위가 10억일때는?
hole = list(map(int, input().split())) # 좌표 압축

# if L == 1:
#     print(N)

# else:
#     cnt = 0
#     x = 0
#     for i in range(len(hole)-1):

#         if L > (hole[i+1] - hole[i]):
#             x += (hole[i+1] - hole[i])   
#             if L > x:
#                 cnt += 1

#         else:
#             x = 0

# print(cnt)
