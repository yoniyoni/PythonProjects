def fabonacci(n):
    if n <= 1:
        return n
    return fabonacci(n - 1) + fabonacci(n - 2)
print("Fibonacci numbers (recursive):")
for i in range(10):
 print(f"Fibonacci({i}) = {fabonacci(i)}")