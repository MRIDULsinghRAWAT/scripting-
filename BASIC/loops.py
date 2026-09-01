#prog for understanding loops

# ===== 1. FOR LOOP =====
print("=== FOR LOOP ===")

# Basic for loop with range
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# For loop with start, stop, step
for i in range(1, 10, 2):
    print(i)  # Output: 1, 3, 5, 7, 9

# For loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# For loop with enumerate (index + value)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")


# ===== 2. WHILE LOOP =====
print("\n=== WHILE LOOP ===")

# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# While loop with break
count = 0
while True:
    if count == 3:
        break  # Exit loop
    print(count)
    count += 1

# While loop with continue
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip this iteration
    print(count)


# ===== 3. NESTED LOOPS =====
print("\n=== NESTED LOOPS ===")

# Nested for loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()  # New line


# ===== 4. LOOP WITH ELSE =====
print("\n=== LOOP WITH ELSE ===")

# For-else: else runs if loop completes normally
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")

# While-else
count = 0
while count < 3:
    count += 1
else:
    print("While loop completed")


# ===== 5. LIST COMPREHENSION =====
print("\n=== LIST COMPREHENSION ===")

# Simple list comprehension
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# With condition
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
