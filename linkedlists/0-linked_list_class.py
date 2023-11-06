
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head

        while temp.next is not None:
            print(temp.value)
            temp = temp.next


    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:

            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value


    def prepend(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head == new_node
            self.tail == new_node
            self.length = 1

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True


    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            self.prepend(value)

        if index == self.length:
            self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True




my_linked_list = LinkedList(2)
my_linked_list.append(3)

my_linked_list.print_list()






my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1

"""

