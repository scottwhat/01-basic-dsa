

# pass in two lists, check if list2 is a subset of list1
def is_subset(list1, list2):

    setList1 = set(list1)

    for num in list2:
        if num not in setList1:
            return False

    return True


list1 = [9, 4, 7, 1, -2, 6, 5]
list2 = [7, 1, 64]
list3 = [10, 12]
print(is_subset(list1, list2))
print(is_subset(list1, list3))
