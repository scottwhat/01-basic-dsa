

class MyHashSet:

    def __init__(self):
        # create a new list node for each position instead of just copyinging it into each
        # if you did [listNode(0)] * 10**4

        # array of ListNodes, all of  these listnodes are the starting of each index in the hashset
        # 10,000 size
        self.set = [ListNode(0) for i in range(10**4)]

        # to add find the index but taking the key and module len(self.set)
        # get the head of that indexs LL with set[index]
    def add(self, key: int) -> None:
        index = key % len(self.set)
        # get head of LL
        cur = self.set[index]

        # iterate to end of the LL and insert
        while cur.next:
            
            # checkfor duplicates and return if dupe.
            if cur.next.key == key:
                return
            cur = cur.next

        cur.next = ListNode(key)

        # to remove again find the LL node,
        # check if the current is the val, otherwise traverse and then find

        # first node is always a dummynode
        # dont need to null check as the nodes all have an empty val node
    def remove(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            # keep moving pointer for list
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next

        # remember to always have an inverse return for T/F
        return False


class ListNode():

    def __init__(self, key):
        self.key = key
        self.next = None
    # resize
    # old hash set becomes temp, init a new hashset of double the size
    # double the element count
    # for each linked list element in the hashset, traverse through and rehash it into the new hashset


# class MyHashSet:
#     def __init__(self):
#         self.arr = set()

#     def add(self, key: int) -> None:
#         self.arr.update({key})

#     def remove(self, key: int) -> None:
#         if key in self.arr:
#             self.arr.remove(key)
#             return True

#     def contains(self, key: int) -> bool:
#         return key in self.arr


# obj = MyHashSet()
# obj.add('58')
# obj.remove(key)
# param_3 = obj.contains(key)
