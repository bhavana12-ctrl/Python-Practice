# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Accessing
print("First fruit:", fruits[0])

# Modifying
fruits[1] = "orange"
print("Modified list:", fruits)

# Adding
fruits.append("grape")
fruits.insert(1, "mango")
print("After adding:", fruits)

# Removing
fruits.remove("apple")
fruits.pop()
print("After removing:", fruits)

# Loop
for fruit in fruits:
    print("Fruit:", fruit)

# List length
print("Total fruits:", len(fruits))

# List comprehension
squares = [x*x for x in range(1, 6)]
print("Squares:", squares)
