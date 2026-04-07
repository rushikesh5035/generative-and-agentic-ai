# List

# In Python there is no Array data type, but there is the List data type that serves the same purpose. Lists are created using square brackets [].
# A list can contain items of different data types, including other lists. Lists are ordered, meaning that the items have a defined order, and they can be accessed using their index.
# List is Mutable, meaning that you can change, add, and remove items in a list after it has been created.

ingredients = ["water", "salt", "pepper", "olive oil"]
print(ingredients)  # Output: ['water', 'salt', 'pepper', 'olive oil']

# Accessing List Items
print(ingredients[0])  # Output: water

# Modifying List Items
ingredients[1] = "sugar"
print(ingredients)  # Output: ['water', 'sugar', 'pepper', 'olive oil']

# Adding Items to a List -> it will append the item to the end of the list
ingredients.append("vinegar")
print(ingredients)  # Output: ['water', 'sugar', 'pepper', 'olive oil', 'vinegar']

# Removing Items from a List
ingredients.remove("pepper")
print(ingredients)  # Output: ['water', 'sugar', 'olive oil', 'vinegar']

spice_options = ["ginger", "cardamom", "cinnamon"]
chai_ingredients = ["water", "milk", "tea leaves"]

# Adding Multiple Items to a List
chai_ingredients.extend(spice_options)
print(chai_ingredients)  # Output: ['water', 'milk', 'tea leaves', 'ginger', 'cardamom', 'cinnamon']

# List Slicing
print(chai_ingredients[0:3])  # Output: ['water', 'milk', 'tea leaves'] index 3 is not included in the output
print(chai_ingredients[3:])   # Output: ['ginger', 'card

# Adding an Item at a Specific Index
chai_ingredients.insert(2, "sugar") # it will insert the item at the specified index and shift the other items to the right
print(chai_ingredients)  # Output: ['water', 'milk', 'sugar', 'tea leaves', 'ginger', 'cardamom', 'cinnamon']

# POP - remove last item from the list and return it
last_added = chai_ingredients.pop() # it will remove the last item from the list and return it
print(last_added)  # Output: cinnamon (the last item in the list)

# Reversing a List
print(chai_ingredients.reverse())  # it will reverse the order of the items in the list
print(chai_ingredients)  # Output: ['cardamom', 'ginger', 'tea leaves', 'sugar', 'milk', 'water']

# Sorting a List
chai_ingredients.sort()  # it will sort the items in the list in alphabetical order
print(chai_ingredients)  # Output: ['cardamom', 'ginger', 'milk', 'sugar', 'tea leaves', 'water']


sugar_levels = [1, 2, 3, 4, 5]
print(f"maximum sugar level: {max(sugar_levels)}")  # Output: maximum sugar level: 5
print(f"minimum sugar level: {min(sugar_levels)}")  # Output: minimum sugar level: 1
print(f"total sugar level: {sum(sugar_levels)}")  # Output: total sugar level: 15 (the sum of all the items in the list)

# **********************************************************************************
# **********************************************************************************

# Operator Overloading with Lists
base_liquid = ["water", "milk"]
extra_flavor = ["honey", "lemon"]

full_liquid= base_liquid + extra_flavor # it will concatenate the two lists and create a new list [this is called operator overloading, where the + operator is overloaded to work with lists]
print(full_liquid)  # Output: ['water', 'milk', 'honey', 'lemon']


raw_spice_data = bytearray(b"CINNAMON") # it will create a bytearray object from the string "CINNAMON"
print(f"Bytes: {raw_spice_data}")  # Output: bytearray(b'CINNAMON')

raw_spice_data = raw_spice_data.replace(b"CINNAMON", b"CARDAMOM") # it will replace the byte string "CINNAMON" with "CARDAMOM" in the bytearray object [this is also an example of operator overloading, where the replace method is overloaded to work with bytearray objects]
print(f"Bytes: {raw_spice_data}")  # Output: bytearray(b'CARDAMOM')
