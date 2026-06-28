# Python Data Types - Complete Notes

## 📘 How Python Works

Python follows a simple flow where code is interpreted line by line.

**Flow:**
Developer → Python Code (.py) → Python Interpreter → Output

**Key Difference from Java:**

- Python is **interpreted** (runs line by line)
- Java is **compiled** (first to bytecode, then executed)

---

## 🔥 Numbers

### Integer (int)

Whole numbers without decimals.

```python
age = 25
temperature = -10
big_number = 1_000_000_000  # Use underscores for readability
```

### Float

Decimal numbers.

```python
price = 19.99
temperature = 36.5
```

### Key Points ⚠️

```python
# By default, decimals are float
a = 23.25      # float
b = 23         # int

# Division always returns float
result = 10 / 2    # 5.0 (not 5)

# Use // for integer division
result = 10 // 3   # 3 (not 3.33)

# Use % for remainder
remainder = 10 % 3  # 1
```

### Arithmetic Operators

```python
5 + 3      # 8 (addition)
5 - 3      # 2 (subtraction)
5 * 3      # 15 (multiplication)
5 / 3      # 1.67 (division)
5 // 3     # 1 (floor division)
5 % 3      # 2 (remainder)
5 ** 3     # 125 (power)
```

---

## 🔥 Booleans

### What is Boolean?

👉 A data type with only two values: **True** or **False**

```python
is_ready = True
is_complete = False
```

### Truthy vs Falsy Values ⚠️

**Falsy values (act like False):**

```python
False, 0, 0.0, "", [], {}, None
```

**Truthy values (act like True):**

```python
True, 1, 2, "hello", [1,2], {"a": 1}
```

### Example

```python
if 1:           # 1 is truthy
    print("✅ Yes")

if "":          # Empty string is falsy
    print("No")
else:
    print("✅ Empty string is False")
```

### Logical Operators

```python
True and False      # False (both must be True)
True or False       # True (at least one True)
not True            # False (negates the value)
```

### Comparison Operators

```python
5 > 3       # True
5 < 3       # False
5 == 5      # True
5 != 3      # True
5 >= 5      # True
```

---

## 🔥 Strings (Immutable ❌ change not allowed)

### What is a String?

👉 A sequence of characters. **IMMUTABLE** = cannot be changed after creation.

```python
text = "Hello World"
# H(0) e(1) l(2) l(3) o(4) (5) W(6)...
```

### Indexing

```python
text = "Hello"

text[0]     # 'H' (first character)
text[-1]    # 'o' (last character)
text[-2]    # 'l' (second last)
```

### Slicing [start:stop:step]

👉 **Important:** stop index is **EXCLUSIVE**

```python
text = "Hello World"

text[0:5]       # "Hello" (positions 0,1,2,3,4)
text[6:]        # "World" (from 6 to end)
text[:5]        # "Hello" (from start to 5)
text[::2]       # "HloWrd" (every 2nd character)
text[::-1]      # "dlroW olleH" (reverse)
```

### ❌ This CANNOT Work (Immutable ❌)

```python
text = "Hello"
text[0] = "J"   # ❌ ERROR! Strings are immutable

# ✅ Correct Way
text = "Jello"  # Create new string
```

### String Methods

```python
text = "hello world"

text.upper()                    # "HELLO WORLD"
text.capitalize()               # "Hello world"
text.replace("world", "python") # "hello python"
text.split()                    # ['hello', 'world']
"-".join(['a', 'b', 'c'])      # 'a-b-c'
text.find("world")              # 6
"world" in text                 # True
len(text)                       # 11
```

### F-strings (Best Way for Formatting)

```python
name = "Sanket"
age = 20

print(f"My name is {name} and I'm {age}")  # My name is Sanket and I'm 20
print(f"Age next year: {age + 1}")         # Age next year: 21
```

### Encoding & Decoding

```python
text = "Hello"
encoded = text.encode('utf-8')  # Convert to bytes: b'Hello'
decoded = encoded.decode('utf-8') # Convert back to string: 'Hello'
```

---

## 🔥 List (Mutable ✅ can change)

### What is a List?

👉 An **ordered** collection that **CAN be changed**. Can contain different data types.

```python
items = ["water", "salt", "pepper"]
numbers = [1, 2, 3, 4, 5]
mixed = ["text", 1, 3.14, True]  # Different types
```

### Accessing & Modifying

```python
items = ["water", "salt", "pepper"]

items[0]        # "water"
items[-1]       # "pepper" (last item)
items[1] = "sugar"  # ✅ Modify item
items.append("oil")  # Add at end
items.insert(1, "milk")  # Add at index 1
items.remove("salt")  # Remove by value
items.pop()      # Remove & return last
items.pop(0)     # Remove & return first
```

### Slicing (Same as Strings)

```python
items = ["a", "b", "c", "d", "e"]

items[0:2]       # ['a', 'b']
items[2:]        # ['c', 'd', 'e']
items[::2]       # ['a', 'c', 'e'] (every 2nd)
items[::-1]      # ['e', 'd', 'c', 'b', 'a'] (reverse)
```

### List Methods

```python
items = ["c", "a", "b"]

items.sort()         # ['a', 'b', 'c'] (sorts in place)
items.reverse()      # Reverse in place
items.index("a")     # 1 (index of item)
items.count("a")     # Count occurrences
len(items)           # 3 (length)
max([1,2,3])         # 3 (max value)
min([1,2,3])         # 1 (min value)
sum([1,2,3])         # 6 (total)
```

### ⚠️ VERY IMPORTANT - Reference vs Copy

```python
list1 = [1, 2, 3]
list2 = list1       # ❌ Same reference (points to same object)

list2[0] = 99
print(list1)        # [99, 2, 3] ❌ list1 is also changed!

# ✅ Correct Way - Create a copy
list2 = list1.copy()  # Different object
list2[0] = 99
print(list1)        # [1, 2, 3] ✅ list1 unchanged
```

**Memory Visualization:**

```
list1 = [1, 2, 3]
list2 = list1

[list1]──┐
         ├──→ [1, 2, 3]  (same memory)
[list2]──┘

vs

list2 = list1.copy()

[list1]──→ [1, 2, 3]
[list2]──→ [1, 2, 3]  (different memory)
```

---

## 🔥 Tuple (Immutable ❌ cannot change)

### What is a Tuple?

👉 An **ordered** collection that **CANNOT be changed**. Use `()`.

```python
spices = ("turmeric", "cumin", "cardamom")
coords = (10, 20, 30)
```

### Accessing (Same as List)

```python
spices = ("turmeric", "cumin", "cardamom")

spices[0]       # "turmeric"
spices[-1]      # "cardamom"
spices[1:3]     # ("cumin", "cardamom")
len(spices)     # 3
```

### ❌ Cannot Modify

```python
spices[0] = "paprika"  # ❌ ERROR! Tuples are immutable
```

### Unpacking 🚀

```python
spices = ("turmeric", "cumin", "cardamom")

# Unpack all
s1, s2, s3 = spices
print(s1)  # "turmeric"

# Swap using tuple unpacking
a, b = 1, 2
a, b = b, a  # ✅ Swap
print(a, b)  # 2 1
```

### Tuple Methods

```python
spices = ("turmeric", "cumin", "turmeric")

spices.count("turmeric")  # 2
spices.index("cumin")     # 1
"turmeric" in spices      # True
```

### 💡 When to Use Tuple?

✔ When you want immutable data (protection)  
✔ Use as dictionary keys  
✔ Return multiple values from function  
✔ Slightly faster than lists

---

## 🔥 Dictionary (Mutable key-value pairs)

### What is a Dictionary?

👉 Stores data as **key-value pairs**. Keys are unique.

```python
order = {"name": "John", "age": 30, "city": "NYC"}
chai = {"type": "Masala", "size": "Large", "sugar": 2}
```

### Accessing & Modifying

```python
order = {"name": "John", "age": 30}

order["name"]              # "John" (raises KeyError if missing)
order.get("name")          # "John"
order.get("price", "N/A")  # "N/A" (default if missing) ✅

order["age"] = 31          # Modify
order["city"] = "NYC"      # Add new
del order["age"]           # Delete
```

### Dictionary Methods

```python
order = {"name": "John", "age": 30, "city": "NYC"}

order.keys()            # ['name', 'age', 'city']
order.values()          # ['John', 30, 'NYC']
order.items()           # [('name', 'John'), ('age', 30), ...]
order.pop("age")        # Remove & return
order.clear()           # Remove all
len(order)              # 3

# Check if key exists
"name" in order         # True
"price" in order        # False
```

### Looping Through Dictionary

```python
order = {"name": "John", "age": 30}

# Loop through keys
for key in order:
    print(key)

# Loop through values
for value in order.values():
    print(value)

# Loop through key-value pairs ✅ Best
for key, value in order.items():
    print(f"{key}: {value}")
```

### Creating & Merging

```python
# Create using dict()
person = dict(name="John", age=30)

# Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Or use update()
dict1.update(dict2)
```

---

## 🔥 Set (Mutable, No Duplicates)

### What is a Set?

👉 An **unordered** collection with **NO duplicates**.

```python
spices = {"cumin", "paprika", "turmeric"}
numbers = {1, 2, 3, 4, 5}

# ⚠️ Empty set must use set(), not {}
empty_set = set()       # ✅ Correct
empty_dict = {}         # ❌ This creates a dict!
```

### Adding & Removing

```python
spices = {"cumin", "paprika"}

spices.add("turmeric")           # Add one
spices.discard("cumin")          # Remove (no error if missing)
spices.remove("paprika")         # Remove (error if missing)
spices.pop()                     # Remove arbitrary item
spices.clear()                   # Remove all
```

### ✅ Duplicates Automatically Removed

```python
items = {1, 2, 2, 3, 3, 3}
print(items)  # {1, 2, 3} ✅ Duplicates gone!
```

### Set Operations 🚀

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Union (all items from both)
set1 | set2         # {1, 2, 3, 4}

# Intersection (common items)
set1 & set2         # {2, 3}

# Difference (in set1 but not set2)
set1 - set2         # {1}

# Symmetric Difference (in either but not both)
set1 ^ set2         # {1, 4}
```

### Check Membership

```python
spices = {"cumin", "paprika", "turmeric"}

"cumin" in spices           # True
"salt" in spices            # False
len(spices)                 # 3
```

---

## 📊 Data Types Comparison Table

| Type       | Mutable | Ordered | Unique | Use Case                          |
| ---------- | ------- | ------- | ------ | --------------------------------- |
| **List**   | ✅      | ✅      | ❌     | Ordered collection that changes   |
| **Tuple**  | ❌      | ✅      | ❌     | Immutable, dict keys, fixed data  |
| **Dict**   | ✅      | ✅      | Keys   | Key-value pairs, fast lookup      |
| **Set**    | ✅      | ❌      | ✅     | Remove duplicates, set operations |
| **String** | ❌      | ✅      | ❌     | Text data                         |

---

## 🔥 Type Conversion vs Type Casting

### Implicit Conversion (Automatic)

```python
# Python automatically converts smaller types to larger
x = 5           # int
y = 3.14        # float
z = x + y       # 8.14 (int converted to float automatically)
```

### Explicit Conversion (Manual)

```python
x = "5"         # string
y = int(x)      # "5" → 5 (int)
z = float(x)    # "5" → 5.0 (float)
s = str(42)     # 42 → "42" (string)
```

### ⚠️ Conversion Errors

```python
int("hello")    # ❌ ValueError! Cannot convert
int("5.5")      # ❌ ValueError! Use float() first
float("5.5")    # ✅ 5.5
```

---

## 🎯 Important Interview Questions

### Q1: What's the difference between == and is?

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# == checks value
print(list1 == list2)   # True (same content)

# is checks reference (memory address)
print(list1 is list2)   # False (different objects)
print(list1 is list3)   # True (same object)
```

### Q2: Why is String immutable?

```python
s = "hello"
s = s + " world"

# ❌ What happens:
# "hello" stays in memory
# New object "hello world" is created
# s now points to new object
# This is inefficient for many changes

# ✅ Use list or join for efficiency
s_list = list("hello")
s_list[0] = 'j'
s = "".join(s_list)  # "jello"
```

### Q3: List vs Tuple - When to use?

```python
# Use LIST when you might modify
fruits = ["apple", "banana", "cherry"]
fruits.append("date")  # ✅ Works

# Use TUPLE for fixed, immutable data
coordinates = (10, 20)  # ❌ Can't change
user_data = ("John", 30, "NYC")  # ✅ Immutable, safe
```

### Q4: How to copy without reference?

```python
original = [1, 2, 3]

# ❌ Wrong - just reference
copy1 = original

# ✅ Correct - shallow copy
copy2 = original.copy()
copy3 = original[:]
copy4 = list(original)

# For nested lists, use deep copy
import copy
copy5 = copy.deepcopy(original)
```

---

## 💡 Key Takeaways

✔ **Immutable types:** String, Tuple, int, float, bool  
✔ **Mutable types:** List, Dictionary, Set  
✔ **Always check references:** Use `.copy()` to avoid reference issues  
✔ **Use the right type:** List for changing data, Tuple for fixed data  
✔ **Slicing:** [start:stop:step] where stop is exclusive  
✔ **Dictionary keys:** Must be immutable (String, Tuple, int)  
✔ **Set operations:** Fast way to remove duplicates and find common elements

---

## 🚀 Quick Cheatsheet

```python
# Create
list = [1, 2, 3]
tuple = (1, 2, 3)
dict = {"key": "value"}
set = {1, 2, 3}
string = "hello"

# Access
item = list[0]
value = dict["key"]
char = string[0]

# Modify (if mutable)
list[0] = 99
dict["key"] = "new"
set.add(4)

# Iterate
for item in list: print(item)
for k, v in dict.items(): print(k, v)

# Check
"key" in dict       # True
1 in list           # True
"h" in string       # True

# Convert
list(tuple)         # List from tuple
dict(list)          # Dict from list of pairs
str(123)            # String from number
```

---

## Run Your Files

```bash
python 01_chapter.py        # Numbers and data type basics
python 02_sets.py           # Set operations
python 03_operators.py      # Operators
python 04_String.py         # Strings and slicing
python 05_Tuples.py         # Tuples and unpacking
python 06_List.py           # Lists
python 08_Dictionary.py     # Dictionaries
python 09_Collections.py    # Named tuples
```
