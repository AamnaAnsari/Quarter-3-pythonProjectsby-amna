def get_first_element(lst):
    # Print the first element of the list
    print("First element:", lst[0])


# Take user input 
n = int(input("How many elements do you want in the list? "))

lst = []
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    lst.append(element)

# Call the function
get_first_element(lst)
