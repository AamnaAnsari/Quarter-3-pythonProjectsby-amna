# Function to return the number of fruits in stock
def num_in_stock(fruit):
    # Inventory for the fruits (example data)
    inventory = {
        "pear": 1000,
        "apple": 500,
        "banana": 0,
        "orange": 300,
        "grape": 150,
    }
    
    #agr fruit exist krta hai too 0 return krega
    return inventory.get(fruit.lower(), 0)

# Main code
def main():
    # Prompt the user to enter a fruit
    fruit = input("Enter a fruit: ").strip()

    # Call num_in_stock to get the number of the fruit in stock
    quantity = num_in_stock(fruit)

    # message print krega quantity ke hisab se 
    if quantity > 0:
        print("This fruit is in stock! Here is how many:")
        print(quantity)
    else:
        print("This fruit is not in stock.")

# Calling the main function to run the program
main()
