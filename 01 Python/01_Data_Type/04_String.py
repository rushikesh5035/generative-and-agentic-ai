# Strings

# String are a sequence of characters. They are immutable, which means that once a string is created, it cannot be changed.

# Core String - "Hello World"
# Indexing - H(0) e(1) l(2) l(3) o(4) (5) W(6) o(7) r(8) l(9) d(10)
# Slicing - [start:stop:step]

chai_type = "Ginger Chai"
customer_name = "John Doe"

print(f"Order for {customer_name}: {chai_type} please!")

chai_description = "Aromatic and Bold"
print(f"Description: {chai_description}")
print(f"First word: {chai_description[0:7]}") # Slicing the first word "Aromati", because the last index is exclusive
print(f"First word: {chai_description[0:8]}")

print(f"Every second character: {chai_description[0:8:2]}") # Slicing every second character - "Aroa nBl"

print(f'Last word: {chai_description[9:]}') # Slicing from index 9 to the end of the string - "and Bold"

print(f'Reversed string: {chai_description[::-1]}') # Reversing the string - "dloB dna citomarA"

label_text = "Chai Special" # 
encoded_label = label_text.encode('utf-8') # Encoding the string to bytes
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode('utf-8') # Decoding the bytes back to string
print(f"Decoded label: {decoded_label}")