# https://leetcode.com/problems/two-sum/

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:

                print(prevMap[diff])
                return [prevMap[diff], i]

            # one pass, if diff not in prevmap, add
            prevMap[n] = i

        return
