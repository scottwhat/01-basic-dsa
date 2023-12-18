
#https://www.educative.io/courses/data-structures-coding-interviews-python/solution-first-non-repeating-integer-in-a-list
# Implement a function, findFirstUnique(lst) that returns the first unique integer in the list. Unique means the number does not repeat and appears only once in the whole list.


def findFirstUnique(lst):
    counts = {}
    counts = counts.fromkeys(lst, 0)
    
    for ele in lst:
        counts[ele] = counts[ele] + 1
    
    answer_key = None
    
    for ele in lst:
        if(counts[ele] is 1):
            answer_key = ele
            break
    
    return answer_key
   
   
   
    
    

print(findFirstUnique([1, 1, 1, 2, 3, 2, 4]))



from collections import OrderedDict

#ordered dictionary
# def findFirstUnique(lst):
#     counts = OrderedDict()
    
#     for ele in lst:
#         if ele in counts:
#             counts[ele] += 1
#         else:
#             counts[ele] = 1
    
#     for key, value in counts.items():
#         if value == 1:
#             return key

#     return None

# print(findFirstUnique([1, 1, 1, 2, 3, 2, 4]))