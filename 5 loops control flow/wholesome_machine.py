# The affirmation 
affirmation = "I am capable of doing anything I put my mind to."

# Loop until the user enters the correct affirmation
while True:
    user_input = input("Please type the following affirmation: ")
    
    if user_input == affirmation:
        print("That's right! :)")
        break  # Exit the loop when the affirmation is correct
    else:
        print("Hmmm That was not the affirmation.")
