import random

# Define the likelihood to stop the counting (DONE_LIKELIHOOD)
DONE_LIKELIHOOD = 0.3  

# The done() function will return True with the likelihood of DONE_LIKELIHOOD
def done():
    return random.random() < DONE_LIKELIHOOD

# The chaotic_counting function 1 se 10 tak count krega lkn maybe jldi stop krde 
def chaotic_counting():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    
    for i in range(1, 11):  # Count from 1 to 10
        if done():  # Check if we should stop
            return  # If done() returns True, stop the function
        
        print(i, end=" ")  # Print the current number without newline
        
    return  # If we reach 10, end the function without calling done()

def main():
    chaotic_counting()
    print("\nI'm done.")

# Run the main function
main()
