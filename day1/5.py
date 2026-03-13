def fibonacci_out(limit):
    memo = [-1] * (limit + 1)
    memo[0], memo[1] = 0, 1
    def fib(n):
        if memo[n] != -1:
            return memo[n]
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    for i in range(limit + 1):
        yield fib(i)
n = int(input("Enter Number of Fibonacci: "))

for num in fibonacci_out(n):
    print(num, end=" ")
