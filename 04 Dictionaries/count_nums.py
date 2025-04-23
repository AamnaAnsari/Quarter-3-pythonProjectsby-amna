# Empty list to store numbers
numbers = []

# Keep asking for numbers until user enters blank
while True:
    user_input = input("Enter a number: ")
    
    if user_input == "":
        break  # stop hojao agr empty input ho too
    
    numbers.append(int(user_input))  # store number as int

count_dict = {}

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# Print results
for number, count in count_dict.items():
    print(f"{number} appears {count} times.")
