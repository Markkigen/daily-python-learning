# Day 2 Project: Simple Age Calculator

# birth year for the user
birth_year = input("Enter your birth year: ")

# Casting 
birth_year = int(birth_year)

# Assume current year is 2025
current_year = 2025

# Calculate age
age = current_year - birth_year

# Show result
print("You are", age, "years old!")
