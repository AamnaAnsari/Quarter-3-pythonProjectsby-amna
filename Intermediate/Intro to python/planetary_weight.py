# Ask for user's Earth weight
earth_weight = float(input("Enter your weight on Earth (in kg): "))

# Calculate Mars weight
mars_weight = earth_weight * 0.378

# Round to 2 decimal places
mars_weight_rounded = round(mars_weight, 2)

# Show result
print("Your weight on Mars would be:", mars_weight_rounded, "kg")
