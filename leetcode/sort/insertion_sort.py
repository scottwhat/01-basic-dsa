

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        # move elements of arr[0,i-1] that are greater than the key
        # to one position ahead of their current

        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j+1] = key

# def insertion_sort(arr):
#     # Traverse through 1 to len(arr)
#     for i in range(1, len(arr)):

#         key = arr[i]

#         # Move elements of arr[0..i-1], that are
#         # greater than key, to one position ahead
#         # of their current position
#         j = i-1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key


# Test the function
arr = [12, 11, 13, 5, 6]

insertion_sort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
