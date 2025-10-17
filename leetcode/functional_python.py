"""
Python Lambda Functions and List Comprehension Tutorial
With examples of functional programming concepts including:
- enumerate, zip, filter, map
- list comprehensions
- lambda functions
- map-reduce patterns
"""

# ---- Lambda Functions ----
# Lambda functions are small anonymous functions with one expression
print("\n=== Lambda Functions ===")

# Traditional function vs Lambda
def add(x, y): 
    return x + y

# Same function as lambda
add_lambda = lambda x, y: x + y

print(f"Regular function: {add(5, 3)}")
print(f"Lambda function: {add_lambda(5, 3)}")

# Common lambda uses:
# 1. Sorting with custom key
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(f"\nSorted by score: {sorted_by_score}")

# 2. Map - apply function to every item
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared}")

# 3. Filter - keep items that return True
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# 4. Reduce - aggregate items
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)
print(f"Sum using reduce: {sum_all}")

# ---- List Comprehension ----
print("\n=== List Comprehension ===")

# Traditional vs List Comprehension
squares_traditional = []
for i in range(5):
    squares_traditional.append(i**2)

# Same with list comprehension
squares_comprehension = [i**2 for i in range(5)]

print(f"Traditional squares: {squares_traditional}")
print(f"Comprehension squares: {squares_comprehension}")

# 1. Basic List Comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"\nEven squares: {even_squares}")

# 2. Nested List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# 3. Multiple if conditions
numbers = range(-5, 5)
positive_even = [x for x in numbers if x > 0 if x % 2 == 0]
print(f"Positive even numbers: {positive_even}")

# 4. if-else in List Comprehension
numbers = range(-5, 5)
categorized = ['positive' if x > 0 else 'negative' if x < 0 else 'zero' for x in numbers]
print(f"Categorized numbers: {categorized}")

# ---- Advanced Functional Concepts ----
print("\n=== Advanced Functional Concepts ===")

# Enumerate - get index and value
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")

# Zip - combine iterables
names = ['Alice', 'Bob']
scores = [95, 87]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Any/All
numbers = [2, 4, 6, 8, 9]
all_even = all(x % 2 == 0 for x in numbers)
any_even = any(x % 2 == 0 for x in numbers)
print(f"All even? {all_even}")
print(f"Any even? {any_even}")

# Practical Examples
print("\n=== Practical Examples ===")

# Example 1: Data Processing
data = [
    {"name": "Alice", "age": 25, "score": 85},
    {"name": "Bob", "age": 22, "score": 92},
    {"name": "Charlie", "age": 28, "score": 78}
]

# Get names of people with score > 80
high_scorers = [person["name"] for person in data if person["score"] > 80]
print(f"High scorers: {high_scorers}")

# Example 2: Dictionary Comprehension
word_lengths = {name: len(name) for name in ['Alice', 'Bob', 'Charlie']}
print(f"Name lengths: {word_lengths}")

if __name__ == "__main__":
    # Practice Exercises:
    # 1. Use lambda to sort strings by length
    # 2. Use list comprehension to get squares of even numbers
    # 3. Combine filter and map to process numbers
    
    # Solutions:
    words = ["python", "is", "awesome"]
    sorted_by_length = sorted(words, key=lambda x: len(x))
    print(f"\nSorted by length: {sorted_by_length}")
    
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"Squares of even numbers: {even_squares}")
    
    numbers = range(-5, 5)
    positive_doubles = list(map(lambda x: x*2, filter(lambda x: x > 0, numbers)))
    print(f"Doubled positives: {positive_doubles}")