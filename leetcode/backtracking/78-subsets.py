# https://neetcode.io/courses/dsa-for-beginners/22

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        #i = value of index making decision on 
        #left and right decisions for each, add num, ignore num each time 
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            # q: what does SOLID stand for? 
            
            dfs(i + 1)

        dfs(0)
        return res


        # @copilot:what does solid stand for in programming?
        
    
    
    
    
