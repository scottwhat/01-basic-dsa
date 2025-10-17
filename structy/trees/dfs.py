def dfs(root, target):
    
    if root is None:
        return False
    
    if root  == target:
        return True
   
    return dfs(root.left, target) or dfs(root.right, target) 
