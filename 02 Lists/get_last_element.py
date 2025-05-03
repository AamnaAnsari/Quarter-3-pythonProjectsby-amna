def get_last_element(lst):
    # Print the last element of the list
    print("Last element:", lst[-1])


# Take user input 
n = int(input("How many elements do you want in the list? "))

lst = []
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    lst.append(element)

# Call the function
get_last_element(lst)
