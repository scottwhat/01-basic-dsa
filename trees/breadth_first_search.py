
#use a queue to process each level of the tree. first in first out to get the left to right 

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs(root):
    queue = deuque()

    if root:
        queue.append(root)
        
    #process each level
    level = 0
    while len(queue) > 0:
        print("Level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1;
        
# #
# def bfs(root):
#     queue = deque()

#     if root:
#         queue.append(root)
    
#     level = 0
#     while len(queue) > 0:
#         print("level: ", level)
#         for i in range(len(queue)):
#             curr = queue.popleft()
#             print(curr.val)
#             if curr.left:
#                 queue.append(curr.left)
#             if curr.right:
#                 queue.append(curr.right)
#         level += 1