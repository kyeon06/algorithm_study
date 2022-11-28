N, k = map(int, input().split())
word = [input() for _ in range(N)]

word = sorted(word) # 사전 순 정렬
word = sorted(word, key=len) # 길이 순으로 정렬

print(word[k-1])