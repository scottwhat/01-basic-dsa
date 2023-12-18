# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            # If the key is greater than the current node's value, go to the right subtree
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # If the key is smaller than the current node's value, go to the left subtree
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                # If the current node has no left child, replace it with its right child
                return root.right
            elif not root.right:
                # If the current node has no right child, replace it with its left child
                return root.left

            # If the current node has both left and right children, find the minimum value in the right subtree
            cur = root.right
            while cur.left:
                cur = cur.left

            # Replace the value of the current node with the minimum value found
            root.val = cur.val
            # Delete the node with the minimum value from the right subtree
            root.right = self.deleteNode(root.right, root.val)

        return root
