class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if node.left is None:
            node.left = Node(data)
        else:
            self._insert_recursive(node.left, data)

        if node.right is None:
            node.right = Node(data)
        else:
            self._insert_recursive(node.right, data)

    def delete_node(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if node.data == key:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.data = successor.data
                node.right = self._delete_recursive(
                    node.right, successor.data)
        elif key < node.data:
            node.left = self._delete_recursive(node.left, key)
        else:
            node.right = self._delete_recursive(node.right, key)

        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def preorder_traversal(self):
        self.__preorder_recursive(self.root)

    def __preorder_recursive(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.__preorder_recursive(node.left)
            self.__preorder_recursive(node.right)
    # def preorder_traversal(self):
    #     self._preorder_recursive(self.root)

    # def _preorder_recursive(self, node):
    #     if node is not None:
    #         print(node.data, end=" ")
    #         self._preorder_recursive(node.left)
    #         self._preorder_recursive(node.right)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is not None:
            self._inorder_recursive(node.left)
            print(node.data, end=" ")
            self._inorder_recursive(node.right)

    def postorder_traversal(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node is not None:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(node.data, end=" ")


# Running the binary tree with dummy data
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print(tree.root.data)
print("Pre-order traversal:")
tree.preorder_traversal()
print("\n")

# print("In-order traversal:")
# tree.inorder_traversal()
# print("\n")

# print("Post-order traversal:")
# tree.postorder_traversal()
# print("\n")
