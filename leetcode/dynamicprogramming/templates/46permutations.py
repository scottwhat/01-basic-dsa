class Solution(object):
    
    def permute(self, nums):
        result = []
        
        
        def backtrack(path):
            
            
            #base case -if path len equals nums
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            #choice: all numbers in nums
            for num in nums:
                #constraint - dont reuse the same number more than once
                if num in path:
                    continue
                
                path.append(num)
                backtrack(paths)
                
                #backtrack, pop last number added 
                path.pop()
                
            backtrack([])
            return result
        
        
#subsets, so it needs to go down the choice trees, and once it hits the base add that to resolved.
#when it returns up it pops off each of the backtracked options. 
