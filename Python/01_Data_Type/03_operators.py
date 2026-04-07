# Numbers, Booleans and Operators

# 1. Numbers
# Integers, Booleans -> True/False
# Real floating -> decimal numbers
# Complex numbers -> 2+3j

import sys
from fractions import Fraction # For exact rational numbers, useful for precise measurements 
from decimal import Decimal # For high precision decimal numbers, useful for financial calculations


black_tea_grams = 14
ginger_grams = 20

total_grams = black_tea_grams + ginger_grams
# print(f"Total grams of base tea: {total_grams}")

remaining_grams = total_grams - ginger_grams
# print(f"Remaining grams of base tea: {remaining_grams}")

milk_liters = 7
serving = 4
milk_per_serving = milk_liters / serving # Float division -> 1.75 liters per serving
# print(f"Milk per serving: {milk_per_serving} liters")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots # Integer division -> 1 tea bag per pot
# print(f"Tea bags per pot: {bags_per_pot}")

total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup # Modulo/remainder operator -> 1 pod left
# print(f"Leftover cardamom pods: {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavor_strength = base_flavor_strength ** scale_factor # Exponentiation -> 8 (2 to the power of 3 -> [2*2*2])
# print(f"Powerful flavor strength: {powerful_flavor_strength}")

total_tea_leaves_harvested = 1_000_000_000 # Underscores in numbers for readability -> 1 billion tea leaves
# print(f"Total tea leaves harvested: {total_tea_leaves_harvested}")
 
# *************************************************************
# *************************************************************
# 2. Booleans

is_boiling = True
stri_count = 5

total_actions = stri_count + is_boiling # true is 1 and false is 0 in Python, so this will be 5 + 1 = 6
# print(f"Total actions: {total_actions}")

milk_present = 0 # false
milk_present = 1 # true
milk_present = "rushi" # non-empty string is true
milk_present = "" # empty string is false
milk_present = None # None is a special value, represent absence of a value. false in boolean context

# print(f"Is milk present? {bool(milk_present)}") # 0 is False, so 0 converts to False


# *************************************************************
# *************************************************************
# 3. Logical Operators 

is_tea_ready = True
is_milk_ready = False
can_serve_tea = is_tea_ready and is_milk_ready # Logical AND -> False (both conditions must be true)
# print(f"Can serve tea? {can_serve_tea}")

can_serve_tea = is_tea_ready or is_milk_ready # Logical OR -> True (at least one condition must be true)
# print(f"Can serve tea? {can_serve_tea}")

can_serve_tea = not is_tea_ready # Logical NOT -> False (negates the value)
# print(f"Can serve tea? {can_serve_tea}")

# 4. Real Numbers and Floating Point Precision

ideal_temp = 85.0
current_temp = 84.99

# print(f"Ideal temperature: {ideal_temp}")
# print(f"Current temperature: {current_temp}")
# print(f"Difference temperature: {ideal_temp - current_temp}") # Due to floating point precision, this may not be exactly 0.00000000000001

# print(sys.float_info) # This will show the precision limits of floating point numbers in Python