def fib(n: int, memo: dict = {}) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

n = int(input())
print(fib(n))
    
