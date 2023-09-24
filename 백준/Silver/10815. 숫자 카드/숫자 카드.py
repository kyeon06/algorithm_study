N = int(input())
dataN = list(map(int, input().split()))
M = int(input())
dataM = list(map(int, input().split()))

data = {}
for n in range(N):
    data[dataN[n]] = 0

for m in range(M):
    if dataM[m] in data:
        print(1, end = " ")
    else:
        print(0, end = " ")