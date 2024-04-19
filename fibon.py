def fibonacci(n):
    fib_sequence = [0, 1] if n > 1 else [0]  # Base cases for Fibonacci sequence
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

n = int(10)
fib_nums = fibonacci(n)
print("nfevewnvfoj3qr", n, "ofjvjew", fib_nums)
