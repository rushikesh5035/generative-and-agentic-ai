# Dictionary  -> Used for storing key-value pairs, ordered, mutable.
# [key]: value

# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values
# print(my_dict) # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
# print(my_dict["name"])  # Output: John
# print(my_dict.get("age"))  # Output: 30

# We can also use the dict() constructor to create a dictionary
chai_order = dict(
    type="Masala Chai",
    size="Large",
    sugar=2
)
# print(f"Chai Order: {chai_order}")

# Creating an empty dictionary and adding key-value pairs
chai_recipe = {}

chai_recipe["water"] = "1 cup"
chai_recipe["milk"] = "1 cup"  
chai_recipe["tea leaves"] = "1 tsp"
chai_recipe["sugar"] = "2 tsp"

# print(f"Chai Recipe: {chai_recipe}")
# print(f"Water: {chai_recipe['water']}") # Output: 1 cup
# print(f"Milk: {chai_recipe['milk']}") # Output: 1 cup

# Deleting a key-value pair from the dictionary
del chai_recipe["sugar"]  # Removing the sugar key-value pair
# print(f"Updated Chai Recipe: {chai_recipe}") # Output: {'water': '  1 cup', 'milk': '1 cup', 'tea leaves': '1 tsp'}


chai_order ={"type": "Masala Chai", "size": "Large", "sugar": 2}

# print(f'Order Details (Keys): {chai_order.keys()}') # Output: dict_keys(['type', 'size', 'sugar'])
# print(f'Order Details (Values): {chai_order.values()}') # Output: dict_values(['Masala Chai', 'Large', 2])

last_item = chai_order.popitem()  # Removes and returns the last key-value pair
print(f"Removed Last Item: {last_item}")  # Output: ('sugar', 2)

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)  # Adding extra spices to the chai recipe
print(f"Updated Chai Recipe with Extra Spices: {chai_recipe}")

chai_size = chai_order["size"]
print(f"Chai size is: {chai_size}")  # Output: Large

chai_size = chai_order.get("customer_name", "Unknown")  # Using get() to avoid KeyError
print(f"Customer Name: {chai_size}")  # Output: Unknown