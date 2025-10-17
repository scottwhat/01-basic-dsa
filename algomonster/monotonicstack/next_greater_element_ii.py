from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []  # monotonic stack storing indices
        
        #circular array, use 2 * n 
        # iterate twice to handle circular array
        # range(2*n) lets us look around the array twice--
        for i in range(2 * n):
            # use i % n to wrap around to start of array
            curr_index = i % n
            
            # while we have elements in stack and current element is greater
            while stack and nums[curr_index] > nums[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = nums[curr_index]
            
            # only add to stack if we're in first iteration
            if i < n:
                stack.append(curr_index)
        
        return result

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: Regular array
    test1 = [1,2,1]
    print(f"Input: {test1}")
    print(f"Output: {sol.nextGreaterElements(test1)}")  # Expected: [2,-1,2]
    
    # Test case 2: Decreasing array
    test2 = [5,4,3,2,1]
    print(f"Input: {test2}")
    print(f"Output: {sol.nextGreaterElements(test2)}")  # Expected: [-1,5,5,5,5]
    
    # Test case 3: Equal elements
    test3 = [1,1,1,1]
    print(f"Input: {test3}")
    print(f"Output: {sol.nextGreaterElements(test3)}")  # Expected: [-1,-1,-1,-1]