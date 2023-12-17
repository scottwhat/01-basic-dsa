list1 = [1, 3, 4, 5]
list2 = [2, 6, 7, 8]

merged_list = []

index_list1 = 0
index_list2 = 0

# process all elements from an entire list

while index_list1 < len(list1) and index_list2 < len(list2):
    if list1[index_list1] < list2[index_list2]:
        merged_list.append(list1[index_list1])
        index_list1 += 1
    else:
        merged_list.append(list2[index_list2])
        index_list2 += 1

for x in range(index_list1, len(list1)):
    merged_list.append(list1[x])

for y in range(index_list2, len(list2)):
    merged_list.append(list2[y])

print(merged_list)


# inplace
list1 = [1, 3, 4, 5]
list2 = [2, 6, 7, 8]

# Ensure list1 has enough space to hold elements of both lists
list1.extend([0] * len(list2))

index_list1 = 0
index_list2 = 0
index_merged = 0

while index_list1 < len(list1) and index_list2 < len(list2):
    if list1[index_list1] <= list2[index_list2] or index_list2 >= len(list2):
        list1[index_merged] = list1[index_list1]
        index_list1 += 1
    else:
        list1[index_merged] = list2[index_list2]
        index_list2 += 1
    index_merged += 1

print(list1)
