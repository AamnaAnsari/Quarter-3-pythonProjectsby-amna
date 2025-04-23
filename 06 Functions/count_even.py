def count_even(lst):
    #  list to store user input integers
    even_count = 0
    
    for num in lst:
        if num % 2 == 0:
            even_count += 1
    
    # Print the count of even numbers
    print(f"Number of even numbers: {even_count}")


def populate_list():
    lst = []
    
    # Prompt the user for input until they press Enter to stop
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        
        # If input is empty (user pressed enter without entering anything), break the loop
        if user_input == "":
            break
        
        try:
            # Convert the input to an integer and append to the list
            num = int(user_input)
            lst.append(num)
        except ValueError:
            # If the input is not a valid integer, ask again
            print("Please enter a valid integer.")
    
    return lst

# count even numbers
def main():
    lst = populate_list()
    count_even(lst)

# Run the main function
main()
