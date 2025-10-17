#https://www.educative.io/courses/data-structures-coding-interviews-python/solution-find-second-maximum-value-in-a-list
#find the second max vlaue in a list

#if looking for values, sort a list first

#1. sort and index
#2. traverse the list twice
#3. second min 1 traversal


#sorted
# def find_second_maximum(lst):
    
#     lst.sort()
#     if len(lst) >= 2:
#         return lst[-2]
    
#     else:
#         return None
    
print(find_second_maximum([9, 2, 3, 6]))


#two loops 
# def find_second_maximum(lst):
    
#     first_max = float('-inf')
#     second_max = float('-inf')
    
#     for num in lst:
#         if num > first_max:
#             first_max = num
            
    
#     for numSecond in lst:
#         if numSecond > second_max and numSecond < first_max:
#             second_max = numSecond
    

#     return second_max
    
# print(find_second_maximum([9, 2, 3, 6]))


#3 one traversal
def find_second_maximum(lst):
   if (len(lst) < 2):
       return
   # initialize the two to infinity
   max_no = second_max_no = float('-inf')
   for i in range(len(lst)):
       # update the max_no if max_no value found
       if (lst[i] > max_no):
           second_max_no = max_no
           max_no = lst[i]
       # check if it is the second_max_no and not equal to max_no
       elif (lst[i] > second_max_no and lst[i] < max_no):
           second_max_no = lst[i]
   if (second_max_no == float('-inf')):
       return
   else:
       return second_max_no


print(find_second_maximum([9, 2, 9, 6,8,7,8,3, 6]))

