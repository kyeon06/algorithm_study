# 카드2 문제, 배열 활용
# 큐를 사용했을 때와 비교했을 경우 시간이 더 오래 걸리는걸 알 수 있다.
# https://www.acmicpc.net/problem/2164

arr = [_ for _ in range(1, int(input()) + 1)]

while len(arr) > 1:
    arr.pop(0)
    arr.append(arr.pop(0))

print(arr[0])
