# Function to print the ones digit of a number
def print_ones_digit(num):
    ones_digit = num % 10  # Get the ones digit using the modulo operator
    print(f"The ones digit is {ones_digit}")

# Main function to execute the program
def main():
    # user se input leta hai 
    num = int(input("Enter a number: "))  # input ko convert krta hai integer main 
    # Call the function to print the ones digit
    print_ones_digit(num)

# Call the main function
main()
