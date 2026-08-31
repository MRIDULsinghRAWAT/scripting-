# code to understand all operators in python
## Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)          # Addition
print("Subtraction:", a - b)       # Subtraction
print("Multiplication:", a * b)    # Multiplication
print("Division:", a / b)          # Division
print("Floor Division:", a // b)   # Floor Division
print("Modulus:", a % b)           # Modulus
print("Exponentiation:", a ** b)   # Exponentiation

## Comparison Operators
x = 5
y = 10
print("Equal:", x == y)             # Equal
print("Not Equal:", x != y)         # Not Equal
print("Greater than:", x > y)       # Greater than
print("Less than:", x < y)          # Less than
print("Greater than or equal to:", x >= y)  # Greater than or equal to
print("Less than or equal to:", x <= y)     # Less than or equal to

## Assignment Operators
c = 5
c += 2  # c = c + 2
print("c after += 2:", c)
c -= 1  # c = c - 1
print("c after -= 1:", c)
c *= 3  # c = c * 3
print("c after *= 3:", c)
c /= 2  # c = c / 2
print("c after /= 2:", c)
c %= 3  # c = c % 3
print("c after %= 3:", c)
c **= 2  # c = c ** 2
print("c after **= 2:", c)

## Logical Operators
p = True
q = False
print("Logical AND:", p and q)      # Logical AND
print("Logical OR:", p or q)        # Logical OR
print("Logical NOT:", not p)        # Logical NOT
print("Logical NOT:", not q)        # Logical NOT


## Membership Operators
my_list = [1, 2, 3, 4, 5]
print("Is 3 in my_list?", 3 in my_list)      # Membership Operator
print("Is 6 not in my_list?", 6 not in my_list)  # Membership Operator


##identity Operators
a = 10
b = 10
print("a is b:", a is b)          # Identity Operator
print("a is not b:", a is not b)  # Identity Operator