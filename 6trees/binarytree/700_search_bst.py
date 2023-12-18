# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node1 = TreeNode(1)
node3 = TreeNode(3)
node5 = TreeNode(5)
node7 = TreeNode(7)
node2 = TreeNode(2, node1, node3)
node6 = TreeNode(6, node5, node7)
root = TreeNode(4, node2, node6)

# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def searchBST(self, root, val):
        if root is None:
            return
        queue = []
        result = []
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            if node.val == val:
                return node
            else:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return


solution = Solution()
print(solution.searchBST(root, 1))
