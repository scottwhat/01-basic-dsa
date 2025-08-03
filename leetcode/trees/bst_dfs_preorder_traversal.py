#pre order - hit a node, do something then go to its children 

def preorder(root):
    if not root:
        return    
    #the do portion 
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    
    