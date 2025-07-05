# Creating tuples
fruits = ("apple", "banana", "cherry")
print("Fruits:", fruits)

# Mixed data types
mixed = (1, "Bhavana", 5.4, True)
print("Mixed tuple:", mixed)

# Accessing items
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Looping
print("Loop through tuple:")
for item in fruits:
    print("-", item)

# Length of tuple
print("Total items:", len(fruits))

# Slicing
print("Sliced tuple:", fruits[1:])

# Nested tuple
student = ("Bhavana", (19, "F"))
print("Nested value:", student[1][0])  # 19

# Tuple with one item
single = ("only_one",)
print("Single-item tuple type:", type(single))

# Immutable test (uncomment to see error)
# fruits[1] = "mango"  # ❌ TypeError
