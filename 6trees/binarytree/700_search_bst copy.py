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

# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         while root!=None and root.val!=val:
#             if val<root.val:
#                 root=root.left
#             else:
#                 root=root.right
#         return root


class Solution:
    def searchBST(self, root, val):
        # Helper method to find the node with the given value
        def findNode(node, val):
            if node is None or node.val == val:
                return node
            elif val < node.val:
                return findNode(node.left, val)
            else:
                return findNode(node.right, val)

        # Helper method to return the subtree rooted with the given node as an array
        def getSubtree(node):
            if node is None:
                return []
            return [node.val] + getSubtree(node.left) + getSubtree(node.right)

        # Find the node with the given value
        targetNode = findNode(root, val)

        # Return the subtree rooted with the target node as an array
        if targetNode is None:
            return []
        else:
            return getSubtree(targetNode)


# Create an instance of the Solution class
solution = Solution()

# Define the value to search for
target_value = 2

# Call the searchBST method and print the result
result = solution.searchBST(root, target_value)
print(result)
