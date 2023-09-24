N, k = map(int, input().split())
data = list(map(int, input().split()))

def cutline(k, data):
    return sorted(data, reverse=True)[k-1]

print(cutline(k, data))
