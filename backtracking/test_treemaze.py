import unittest

from treemaze import leafPath

class TestLeafPath(unittest.TestCase):
    def test_leaf_path(self):
        # Test case 1: Leaf path exists
        #       1
        #      / \
        #     2   3
        #    / \   \
        #   4   5   6
        #  /
        # 7
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        root.left.left.left = TreeNode(7)

        path = []
        self.assertTrue(leafPath(root, path))
        self.assertEqual(path, [1, 2, 4, 7])

        # Test case 2: Leaf path does not exist
        #       1
        #      / \
        #     2   3
        #    / \   \
        #   4   0   6
        #  /
        # 7
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(0)
        root.right.right = TreeNode(6)
        root.left.left.left = TreeNode(7)

        path = []
        self.assertFalse(leafPath(root, path))
        self.assertEqual(path, [])

if __name__ == '__main__':
    unittest.main()