# Problem 1: Bitwise AND
# Write a function that takes two integers and returns their bitwise AND.
def bitwise_and(a, b):
    # The & operator performs a bitwise AND operation.
    return a & b

# Problem 2: Bitwise OR
# Write a function that takes two integers and returns their bitwise OR.
def bitwise_or(a, b):
    # The | operator performs a bitwise OR operation.
    return a & b

# Problem 3: Bitwise XOR
# Write a function that takes two integers and returns their bitwise XOR.
def bitwise_xor(a, b):
    # The ^ operator performs a bitwise XOR operation.
    return a ^ b

# Problem 4: Bitwise NOT
# Write a function that takes an integer and returns its bitwise NOT.
def bitwise_not(a):
    # The ~ operator performs a bitwise NOT operation.
    return ~a

# Problem 5: Bitwise Left Shift
# Write a function that takes an integer and a shift count, and returns the integer left-shifted by the shift count.
def left_shift(a, shift):
    # The << operator performs a left shift operation.
    return a << shift

# Problem 6: Bitwise Right Shift
# Write a function that takes an integer and a shift count, and returns the integer right-shifted by the shift count.
def right_shift(a, shift):
    # The >> operator performs a right shift operation.
    return a >> shift

# Problem 7: Check if a number is even or odd using bitwise operations
# Write a function that takes an integer and returns True if it is even, and False if it is odd.
def is_even(a):
    # The & operator can be used to check the least significant bit.
    return (a & 1) == 0

# Problem 8: Swap two numbers using bitwise XOR
# Write a function that takes two integers and swaps their values using bitwise XOR.
def swap(a, b):
    # XOR swap algorithm
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# Problem 9: Count the number of 1 bits in an integer
# Write a function that takes an integer and returns the number of 1 bits in its binary representation.
def count_ones(a):
    count = 0
    while a:
        count += a & 1
        a >>= 1
    return count

# Problem 10: Determine if a number is a power of two
# Write a function that takes an integer and returns True if it is a power of two, and False otherwise.
def is_power_of_two(a):
    # A number is a power of two if it has exactly one 1 bit in its binary representation.
    return a > 0 and (a & (a - 1)) == 0