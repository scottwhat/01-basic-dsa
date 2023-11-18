def preorder(root):
    if not root:
        return    
    print(root.val)
    preorder(root.left)
    preorder(root.right)