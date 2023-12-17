# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# https://www.youtube.com/watch?v=ihj4IQGZ2zc&embeds_referring_euri=https%3A%2F%2Fneetcode.io%2F&source_ve_path=MjM4NTE&feature=emb_title

#recursive tree build 
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        #mid + 1 is non inclusive 
        #inoder[:mid] non inclusive 
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root