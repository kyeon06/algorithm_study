# 메모리 : 31256KB / 시간 : 80ms

N = int(input())
arr = [int(input()) for i in range(N)]

for num in sorted(arr):
    print(num)