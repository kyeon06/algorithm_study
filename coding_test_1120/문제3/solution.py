subject_cnt = int(input())
arr = [list(map(int, input().split())) for _ in range(subject_cnt)]

def check(arr):
    result = 0
    cutline = arr[0]*(arr[2]*0.01)

    if arr[1] < cutline :
        result = 1
        for i in range(arr[3]):
            if arr[4] > arr[i+5]:
                result = 0
                break;
    return result


	
result=[]
for i in range(len(arr)):
    result.append(check(arr[i]))

if sum(result) == subject_cnt:
    print(1)
else :
    print(0)