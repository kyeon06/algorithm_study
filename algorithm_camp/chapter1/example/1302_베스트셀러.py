# 베스트 셀러 / 집합과 맵 사용
# https://www.acmicpc.net/problem/1302

d = {}

for _ in range(int(input())):
    title = input()

    if title in d:
        d[title] += 1
    else:
        d[title] = 1

# 먼저 가장 많이 팔린 책의 개수를 구한다
max_sell = max(d.values())
# 해당 숫자에 해당하는 책 이름을 저장한다
bestseller = [k for k, v in d.items() if v == max_sell]

# 그 중에 알파벳 순으로 정렬하여 결과를 반환한다
bestseller.sort()
print(bestseller[0])