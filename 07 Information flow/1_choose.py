# constant for age 
ADULT_AGE = 18

# Function to check if the person is an adult
def is_adult(age):
    if age >= ADULT_AGE:
        return True
    else:
        return False

# age input leta ha user se 
user_input = input("How old is this person?: ")
age = int(user_input)

# Call the function and print the result
print(is_adult(age))
