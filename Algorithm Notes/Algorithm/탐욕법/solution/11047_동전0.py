# 동전 0
# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())

money = [int(input()) for _ in range(N)]

cnt = 0
for i in sorted(money, reverse=True):

    if K >= i:

        # 개수
        cnt += K // i
        
        # 남은 돈 계산
        K %= i

print(cnt)