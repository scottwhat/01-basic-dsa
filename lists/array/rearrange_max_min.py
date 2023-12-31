
# i received a sorted list!!!

# Define a function named max_min that takes a list as input
def max_min(lst):
    # Create an empty list to store the rearranged elements
    result = []
    # Iterate over half of the length of the input list
    for i in range(len(lst)//2):
        # Append the i-th element from the end of the list to the result list
        result.append(lst[-(i+1)])
        # Append the i-th element from the start of the list to the result list
        result.append(lst[i])
    # If the length of the list is odd, append the middle element to the result list
    if len(lst) % 2 == 1:
        result.append(lst[len(lst)//2])
    # Return the rearranged list
    return result


# Dummy data
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call the function
print(max_min(lst))
