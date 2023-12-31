# def generateBinaryStrings(n, arr, i):
#     if i == n:
#         print("".join(arr))
#         return
#     # First assign "0" at ith position
#     # and try for all other permutations
#     # for remaining positions
#     arr[i] = "0"
#     generateBinaryStrings(n, arr, i + 1)

#     # And then assign "1" at ith position
#     # and try for all other permutations
#     # for remaining positions
#     arr[i] = "1"
#     generateBinaryStrings(n, arr, i + 1)


# # Driver Code
# n = 3
# arr = [""] * n
# result = generateBinaryStrings(n, arr, 0)
# print


#driver 



def generateBinaryStrings(n, arr, i):
    
    
#driver 
n = 3

arr = []

