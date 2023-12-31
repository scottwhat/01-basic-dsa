# options
# for loop traversal. check if positive or negative, if negative, pop and insert at sstart

# list comprehension, with lambdass
# CAN JUST SORT
# OR DO SWAPS (SORTING) in place list[elk]


def rearrange(list):

    new_list_negatives = [num for num in list if num < 0]
    new_list_positives = [num for num in list if num >= 0]

    return new_list_negatives + new_list_positives


# def rearrange(list):

#     for num in lists:

#         results = []
#         if num < 0:
#             results.append(num)

#         else:
#             results.insert(0, num)
