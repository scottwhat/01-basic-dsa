
# DFS
def preorder(self, root):
    if not root:
        return []
    ret = []
    stack = [root]
    while stack:
        node = stack.pop()
        ret.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return ret


def postorder(self, root):
    if not root:
        return []
    from collections import deque
    ret = deque()
    stack = [root]
    while stack:
        node = stack.pop()
        ret.appendleft(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ret


def inorder(self, root):
    if not root:
        return []
    ret = []
    stack = []
    while root is not None or stack:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        ret.append(root.val)
        root = root.right
    return ret

# BFS


def levelorder(self, root):
    if not root:
        return []
    ret = []
    from collections import deque
    queue = deque([root])
    while queue:
        ret_row = []
        # fixed size for current level
        for _ in range(len(queue)):
            node = queue.popleft()
            ret_row.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ret.append(ret_row)
    return ret
