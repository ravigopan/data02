def fibonacci(n):
    fib_series = [0, 1]  # Initialize Fibonacci series with first two terms
    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]  # Compute next term
        fib_series.append(next_term)  # Add next term to the series
    return fib_series

# Function to print Fibonacci series up to n terms
def print_fibonacci_series(n):
    fib_series = fibonacci(n)
    print("Fibonacci Series up to", n, "terms:")
    for num in fib_series:
        print(num, end=" ")

# Example usage:
num_terms = 10  # Change this value to print more or fewer terms
print_fibonacci_series(num_terms)
