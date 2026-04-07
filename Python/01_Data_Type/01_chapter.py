# Data Types
# Declare a variable to store the amount of sugar

sugar_amount = 12
print(f"Amount of sugar: {sugar_amount}")

sugar_amount = 15
print(f"Updated amount of sugar: {sugar_amount}") # Reassigning the variable to a new value(mutable)

# Python will never change the value 12 to 15. it will create new number 15 and pointing from 12 to 15. So, 12 is immutable and 15 is mutable. (We just change the reference of variable)

print(f"ID of 12: {id(12)}") # identity of object 12
print(f"ID of 15: {id(15)}") # identity of object 15