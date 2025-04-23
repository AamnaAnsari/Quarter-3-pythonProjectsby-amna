# Function to print divisors of a number
def print_divisors(num):
    # heading print krega
    print(f"Here are the divisors of {num}")
    
    # Loop through numbers from 1 to num
    for i in range(1, num + 1):
        if num % i == 0:  # Check if i is a divisor of num
            print(i, end=" ")

# Main function to execute the program
def main():
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))
    
    # Call the print_divisors function
    print_divisors(num)

# Call the main function
main()
