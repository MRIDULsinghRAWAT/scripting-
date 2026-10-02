# prog to understand a basic func.
def greet(name):
    """Function to greet a person by name."""
    return f"Hello, {name}!"


def add(a, b):
    """Function to add two numbers."""
    return a + b


def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b


if __name__ == "__main__":
    # Test the functions
    print(greet("Alice"))
    print(greet("Bob"))
    
    result1 = add(5, 3)
    print(f"5 + 3 = {result1}")
    
    result2 = multiply(4, 7)
    print(f"4 × 7 = {result2}")
