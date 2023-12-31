def right_rotate(lst, k):
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)

    # return lst[-k:] + lst[:-k]
    print(lst[-k:])
    print(lst[:-k])

    return lst[-k:] + lst[:-k]


list1 = [1, 3, 4, 5]
list2 = [2, 6, 7, 8]

k = 2

right_rotate(list1, k)
right_rotate(list2, k)
