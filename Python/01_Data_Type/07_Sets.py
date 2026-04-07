# Sets  -> Used for storing unique values, unordered, mutable.

# Sets are unordered collections of unique elements. They are mutable, meaning you can add or remove items after creation. Sets are defined using curly braces {} or the set() constructor.

essential_spices = {"cardamom", "cinnamon", "clove", "ginger"}
optional_spices = {"nutmeg", "ginger", "turmeric", "clove"}

all_spices = essential_spices.union(optional_spices) # Union of two sets (combines all unique elements)
print("All Spices:", all_spices) # Output: All Spices: {'cinnamon', 'nutmeg', 'cardamom', 'clove', 'ginger', 'turmeric'}

common_spices = essential_spices.intersection(optional_spices) # Intersection of two sets (elements common to both sets)
print("Common Spices:", common_spices) # Output: Common Spices: {'ginger', 'clove'}

only_in_essential = essential_spices - optional_spices # Difference of two sets (elements in essential_spices but not in optional_spices)
# OR
# only_in_essential = essential_spices.difference(optional_spices)

print("Only in Essential Spices:", only_in_essential) # Output: Only in Essential Spices: {'cinnamon', 'cardamom'}


# ----------Check for membership----------
print(f"Is 'clove' an essential spice? {'clove' in essential_spices}") # Output: Is 'clove' an essential spice? True
print(f"Is 'turmeric' an essential spice? {'turmeric' in essential_spices}") # Output: Is 'turmeric' an essential spice? False

