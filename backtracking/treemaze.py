def leafPath(root, path):

    if not root or root.val == 0:
        return False

    path.append(root.val)

    # made to leaf node
    if not root.left and not root.right:
        return True

    if leafPath(root.left, path):
        return True

    if leafPath(root.right, path):
        return True

    path.pop()

    return False


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_dummy_tree():
    # Create a binary tree with some nodes and values
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.right.left.left = TreeNode(12)
    root.right.left.right = TreeNode(13)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(15)

    return root


print_tree(create_dummy_tree())
# Test the leafPath function with the dummy tree
root = create_dummy_tree()
path = []
result = leafPath(root, path)
print("Path:", path)
print("Result:", result)
