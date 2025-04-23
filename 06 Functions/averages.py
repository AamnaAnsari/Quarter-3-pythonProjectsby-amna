def calculate_average(num1, num2):
    # Calculate the average of the two numbers
    average = (num1 + num2) / 2
    return average

# function ko test krta hai 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function and print the result
average = calculate_average(num1, num2)
print(f"The average of {num1} and {num2} is {average}")
