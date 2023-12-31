def right_rotate(lst, k):
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)

    # return lst[-k:] + lst[:-k]
    print(lst[-k:])
    print(lst[:-k])
    # - starst from the end, gets the k last elements
    # :-k starts from start and removes k last elemenbts,
    # add them in reversed order
    return lst[-k:] + lst[:-k]


list1 = [1, 3, 4, 5]
list2 = [2, 6, 7, 8]

k = 2
