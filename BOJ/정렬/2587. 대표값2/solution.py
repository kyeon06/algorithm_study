# 메모리 : 31256KB / 시간 : 40ms

arr = [int(input()) for n in range(5)]

arr = sorted(arr)

print( int(sum(arr) / len(arr)) )
print( arr[2] )