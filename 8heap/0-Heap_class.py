

24 - Push and Pop

Suggested Problems

Status
Star
Problem   
Difficulty   
Video Solution
Code
Kth Largest Element In a Stream	
Heaps Push and Pop
Push
Taking the same binary heap from before: [14,19,16,21,26,19,68,65,30,null,null,null,null,null,null], let's say we wish to push 17. We need to make sure we push 17 such that we maintain our structure and order property.

Since a binary heap is a complete binary tree, and we are required to fill nodes in a contigious fashion, pushing 17 should happen at the 
10
10th index. However, this might violate the min heap property, which means we will have to percolate 17 up the tree until we find its correct position.

In this case, because 17 is less than its parent, 26, it needs to percolate up until it is no longer less than its parent. So, we swap 17 with 26 and now 17's parent is 19, which again violates the min-heap property. We perform another swap. After that 17 is now greater than its new parent, which is 14. 17 is also smaller than all of its descendents because 19 was already smaller than all of its descendents. The resulting min-heap would look like the following.

dsa-heaps-pushandpop

def push(self, val):
    self.heap.append(val)
    i = len(self.heap) - 1

    # Percolate up
    while i > 1 and self.heap[i] < self.heap[i // 2]:
        tmp = self.heap[i]
        self.heap[i] = self.heap[i // 2]
        self.heap[i // 2] = tmp
        i = i // 2
The "//" indicates taking the floor of the resulting answer so we can round down, e.g. 
5.5
5.5 becomes 
5
5 since indices are whole numbers.
Since we know the tree will always be balanced, the time complexity of the push operation is 
�
(
�
�
�
 
�
)
O(log n).

Pop
The obvious way
Popping from a heap is more complicated than the push operation. One way that you might have already thought about is pop the root node and replace it with min(left_child, right_child). The issue here is that while the order property is intact, we have violated the structure property. Taking the tree from before, popping 14, and swapping it with 16 - min(left_child, right_child) would require 19 to replace 16. Now, level 
2
2 has a missing node i.e 19 is missing a left child.

The correct way
The correct way is to take the right-most node of the last level and swap it with the root node. We have now maintained the structure property. However, the order property is violated. To fix the order property, we have to make sure that 30 finds its place. To do so, we will run a loop and swap 30 with min(left_child, right_child). We swap 30 with 16, then 19 with 30. The resulting tree will look like the following.

dsa-heaps-pushandpop

def pop(self):
    if len(self.heap) == 1:
        return None
    if len(self.heap) == 2:
        return self.heap.pop()

    res = self.heap[1]   
    # Move last value to root
    self.heap[1] = self.heap.pop()
    i = 1
    # Percolate down
    while 2 * i < len(self.heap):
        if (2 * i + 1 < len(self.heap) and 
        self.heap[2 * i + 1] < self.heap[2 * i] and 
        self.heap[i] > self.heap[2 * i + 1]):
            # Swap right child
            tmp = self.heap[i]
            self.heap[i] = self.heap[2 * i + 1]
            self.heap[2 * i + 1] = tmp
            i = 2 * i + 1
        elif self.heap[i] > self.heap[2 * i]:
            # Swap left child
            tmp = self.heap[i]
            self.heap[i] = self.heap[2 * i]
            self.heap[2 * i] = tmp
            i = 2 * i
        else:
            break
    return res
The pseudocode shown above might seem daunting at first so let's go over it. If our heap is empty, there is nothing to pop, hence the return null. Our heap also could have just one node, in which case, we will just pop that node and don't need to make any adjustments. If the above two statements have not executed, it must be the case that we have children, meaning we need to perform a swap.

We store our 14 into a variable called res so that we don't lose it. Then, we can pop from our heap, and replace 30 to be at the root node.

Our while loop runs as long as we have a left child and we determine this by making sure 2 * i is not out of bounds. Then, there are three cases we concern ourselves with:

The node has no children
The node only has a left child
The node has two children
When considering a binary heap, it is not possible to have only a right child because then it no longer is a complete binary tree and violates the structure property.
Because we are guarenteed to have a left child in the while loop, we need to now check if the node also has a right child, which we check by 2 * i + 1. We also make sure that the current node is greater than its children because of the order property. We replace the node with the minimum of its two children.

If no right child exists and the current node's value is greater than its left child, we swap it with the left child.

If none of the above cases exectue, then it must be the case that our node is in the proper position already, satisfying both the order and the structural property.

Closing Notes
The time complexity of the operations discussed so far can be summarized by the following table.

Operation	Big-O Time
Get Min/Max	
�
(
1
)
O(1)
Push	
�
(
�
�
�
 
�
)
O(log n)
Pop	
�
(
�
�
�
 
�
)
O(log n)
# Min Heap
class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        # Percolate up
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]   
        # Move last value to root
        self.heap[1] = self.heap.pop()
        i = 1
        # Percolate down
        while 2 * i < len(self.heap):
            if (2 * i + 1 < len(self.heap) and 
            self.heap[2 * i + 1] < self.heap[2 * i] and 
            self.heap[i] > self.heap[2 * i + 1]):
                # Swap right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                # Swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res

    def top(self):
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    def heapify(self, arr):
        # 0-th position is moved to the end
        arr.append(arr[0])

        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            # Percolate down
            i = cur
            while 2 * i < len(self.heap):
                if (2 * i + 1 < len(self.heap) and 
                self.heap[2 * i + 1] < self.heap[2 * i] and 
                self.heap[i] > self.heap[2 * i + 1]):
                    # Swap right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    # Swap left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            cur -= 1
