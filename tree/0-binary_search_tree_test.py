class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root is None:
        return    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# Example usage:
# Create an empty root
root = None

# Insert elements into the tree
keys = [5, 3, 7, 2, 4, 6, 8]
for key in keys:
    root = insert(root, key)

# Test the inorder function
inorder(root)


def preorder(root):
    if not root:
        return    
    #the do portion 
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    
def postorder(root):
    if not root:
        return    
    postorder(root.left)
    postorder(root.right)
    print(root.val)