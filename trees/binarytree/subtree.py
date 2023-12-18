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


def getSubTreeArray(root):
    if root is None:
        return []
    leftSubtree = getSubTreeArray(root.left)
    rightSubTree = getSubTreeArray(root.right)
    return [root.val] + leftSubtree + rightSubTree
#


print(getSubTreeArray(root))
