def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# Generate Fibonacci series up to the nth term
n_terms = 10  # You can change this value to generate more terms
print("Fibonacci series:")
for i in range(1, n_terms + 1):
    print(fibonacci(i), end=" ")