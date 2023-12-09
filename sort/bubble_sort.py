# steps
# passs the array until all elements are sorted

def bubble_sort(arr):

    n = len(arr)
    for i in range(n):
        # last i elements have already been sorted
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# def bubble_sort(arr):
#     n = len(arr)

#     # Traverse through all array elements
#     for i in range(n):

#         # Last i elements are already in place
#         for j in range(0, n-i-1):

#             # Traverse the array from 0 to n-i-1
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# Test the function
arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
