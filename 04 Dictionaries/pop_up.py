# Dictionary with fruit prices
fruit_prices = {
    "apple": 1.5,
    "durian": 5.0,
    "jackfruit": 2.0,
    "kiwi": 3.0,
    "rambutan": 4.0,
    "mango": 2.5
}

# Variable jo cost ko hold krega 
total_cost = 0

# user se quantity pochega 
for fruit, price in fruit_prices.items():
    quantity = int(input(f"How many ({fruit}) do you want?: "))
    total_cost += quantity * price

# Print the total cost
print(f"Your total is ${total_cost}")
