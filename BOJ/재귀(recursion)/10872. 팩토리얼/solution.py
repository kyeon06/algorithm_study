N = int(input())

def factorial(n):
    # 1! = 1
    if n == 1 or n == 0:
        return 1
    # (n이 2 이상의 수일 때) n! = n * (n-1)!
    elif n >= 2:
        return n * factorial(n - 1)

print(factorial(N))