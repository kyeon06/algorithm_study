N = int(input())

memo = {0: 0, 1: 1}

def f(n):
    if n in memo:
        return memo[n]

    else:
        temp = f(n - 1) + f(n - 2)
        memo[n] = temp
        return temp

print(f(N))