def factorial(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Sample call
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
