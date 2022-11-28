def get_width(arr):
    width = []
    for line in arr:
        for idx, value in enumerate(line):
            if(value==1):
                width.append(idx)
    return max(width) - min(width) + 1
	

def get_height(arr):
    height = [idx for idx, line in enumerate(arr) if sum(line)>0]
    return max(height) - min(height) + 1

size = int(input())
arr = [list(map(int, input().split())) for _ in range(size)]	

width = get_width(arr)
height = get_height(arr)
print(width*height)