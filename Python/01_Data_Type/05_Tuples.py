# Tuples

# Tuples is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples -> () - immutable

masala_spices = ("haldi", "mirch", "dhaniya", "jeera")
print(masala_spices)
print(type(masala_spices))

(spice1, spice2, spice3, spice4) = masala_spices
print(f"Main masala spice: {spice1}, {spice2}, {spice3}")

ginger_ratio, cadramom_ratio = 2, 1 # 
print(f"Ratio of ginger: {ginger_ratio}, and cardamom: {cadramom_ratio}")

ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio # swapping values
print(f"After swapping, ratio of ginger: {ginger_ratio}, and cardamom: {cadramom_ratio}")

# ************************************************************************
# ************************************************************************

# Membership of tuples
# Check if a spice is in the tuple 
# Note: 'in' operator is used to check if an element exists in a tuple. It returns True if the element is found, otherwise it returns False.

print(f"Is ginger in masala spices? {'ginger' in masala_spices}")
print(f"Is dhaniya in masala spices? {'dhaniya' in masala_spices}")