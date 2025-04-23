# Minimum height requirement
minimum_height = 50

while True:
    # Get user input
    user_input = input("How tall are you? ")

    # If user presses Enter without typing, stop
    if user_input == "":
        print("Goodbye!")
        break

    # Convert to integer
    height = int(user_input)

    # Check height
    if height >= minimum_height:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")
