#https://leetcode.com/problems/kth-smallest-element-in-a-bst/
#https://www.youtube.com/watch?time_continue=35&v=5LUXSvjmGCw&embeds_referring_euri=https%3A%2F%2Fneetcode.io%2F&source_ve_path=MjM4NTE&feature=emb_title

#kth is the position that you want the smallest value, so stack them all up, then  pop off
#reducing k -= 1 on pop
# set cur to stack.pop 
#if k = 0 return current 

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop() 
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
            

# class Solution:

#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         stack, cur = [], root # first in, last out
        
#         # iterative in-order DFS traversal
#         while True:
#             while cur: # go as left as possible
#                 stack.append(cur)
#                 cur = cur.left

#             cur = stack.pop() # last one, smallest node
#             k -= 1
#             if k == 0:
#                 return cur.val
                
#             cur = cur.right