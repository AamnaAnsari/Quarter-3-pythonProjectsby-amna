def print_even_odd():
    # Iterate over the range of numbers from 10 to 19
    for num in range(10, 20):
        if num % 2 == 0:  # check krega agr number even hoga too
            print(f"{num} even")
        else:  # If it's not even, it must be odd
            print(f"{num} odd")

# Call the function to print the sequence
print_even_odd()
