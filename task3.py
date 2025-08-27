import math

# Ask user for input
num = float(input("Enter a number: "))

# Perform calculations
sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)

# Display results
print(f"Square root of {num}: {sqrt_val}")
print(f"Natural logarithm of {num}: {log_val}")
print(f"Sine of {num} (in radians): {sine_val}")
