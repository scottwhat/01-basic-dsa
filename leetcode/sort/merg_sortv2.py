
def merge(arr, s, m, e):
    leftArray = arr[s: m+1]
    rightArray = arr[:m + 1: e + 1]
    
    leftIndex = 0
    rightIndex = 0
    arrIndex = 0
    
    while leftIndex < len(leftArray) and rightIndex < len(rightArray):
        
        #merging lists 
        if leftArray[leftIndex] <= rightArray[rightIndex]:
            arr[arrIndex] = leftArray[leftIndex]
            leftIndex += 1
            
        else:
            arr[arrIndex] = rightArray[rightIndex]
            rightIndex += 1
        
        arrIndex += 1
        
        
    #check wwhich half has elements remaining and add to end
    while leftIndex < len(leftArray):
        arr[arrIndex] = leftArray[leftIndex]
        leftIndex += 1
        arrIndex += 1
    
    while rightIndex < len(rightArray):
        arr[arrIndex] = rightArray[rightIndex]
        rightIndex += 1
        arrIndex += 1


def mergeSort(arr, s, e):
    #check if array length 1
    if e - s + 1 <= 1:
        return arr

    # The middle index of the array
    m = (s + e) // 2

    # Sort the left half
    mergeSort(arr, s, m)

    # Sort the right half
    mergeSort(arr, m + 1, e)

    # Merge sorted halfs
    merge(arr, s, m, e)
    
    return arr

    
original_list = [3, 1, 4, 2]
print('Original List:', original_list)


sorted_list = mergeSort(original_list, 0, len(original_list) - 1)


print('\nSorted List:', sorted_list)