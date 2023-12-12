def find_sum(lst, k):
    # Create a dictionary to store the count of each number
    count = {}
    for num in lst:
        count[num] = count.get(num, 0) + 1

    index1 = 0
    index2 = len(lst) - 1
    result = []
    sum = 0

    while index1 != index2:
        sum = lst[index1] + lst[index2]
        if sum < k:
            index1 += 1
        elif sum > k:
            index2 -= 1
        else:
            # Check if both numbers have sufficient count
            if count[lst[index1]] > 1 and count[lst[index2]] > 1:
                result.append(lst[index1])
                result.append(lst[index2])
                return result
            else:
                index1 += 1
                index2 -= 1

    return False
