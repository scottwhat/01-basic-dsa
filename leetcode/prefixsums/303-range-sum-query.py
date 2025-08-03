https://leetcode.com/problems/range-sum-query-immutable/

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]



class NumArray:
    
    def __init__(self, nums):
        
        self.prefix = []
        
        cur = 0
        
        for n in nums: 
            cur += n
            self.prefix.append(cur)
            
    
    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        #to account for index[0]
        #first index left is always the same as the input arrays [0] val anyway
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return rightSum - leftSum