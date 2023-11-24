# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        L = 1
        
        for r in range(1, len(nums)):
            
            if nums[r] != nums[r - 1]:
                nums[L] = nums[r]
                L += 1
            #increment r by the for loop
        return L    
        