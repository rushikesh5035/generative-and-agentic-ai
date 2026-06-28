# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

spice_mix = set()

print(f"initial spice mix: {spice_mix}")
print(f"initial spice mix id: {id(spice_mix)}")

spice_mix.add("cumin")
spice_mix.add("paprika")

print(f"spice mix after adding elements: {spice_mix}")
print(f"After adding elements, ID of spice mix: {id(spice_mix)}")

# initial spice mix id: 1554215962656
# After adding elements, ID of spice mix: 1554215962656

# The ID of the spice mix remains the same after adding elements, which shows that the set is mutable. We can change its contents without changing its identity.

# Adding an empty string to the set
spice_mix.add("")
print(f"spice mix after adding elements: {spice_mix}")

spice_mix.add("cumin") # Adding duplicate element, it will not be added to the set
print(f"spice mix after adding duplicate element: {spice_mix}") # unchanged