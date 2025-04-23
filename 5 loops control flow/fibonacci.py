# Constant maximum value
MAX_VALUE = 10000

fib_0 = 0
fib_1 = 1

# Print the first term (Fib(0))
print(fib_0, end=" ")

# Loop to print Fibonacci sequence terms less than MAX_VALUE
while fib_1 <= MAX_VALUE:
    print(fib_1, end=" ")
    # Update the next Fibonacci term
    fib_0, fib_1 = fib_1, fib_0 + fib_1
