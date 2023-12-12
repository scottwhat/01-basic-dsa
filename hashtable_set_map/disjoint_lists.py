# You have to implement the is_disjoint() function which checks whether two given lists are disjoint or not. Two lists are disjoint if there are no common elements between them. The assumption is that there are no duplicate elements in each list.
list1 = [9, 4, 3, 1, -2, 6, 5]
list2 = [7, 10, 8]


def is_disjoint(list1, list2):

    set1 = set(list1)

    for num in list2:
        if num in set1:
            return False

    return True


list1 = [9, 4, 3, 1, -2, 6, 5]
list2 = [7, 10, 8]
list3 = [1, 12]
print(is_disjoint(list1, list2))
print(is_disjoint(list1, list3))
