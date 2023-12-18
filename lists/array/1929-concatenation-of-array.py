# https://leetcode.com/problems/concatenation-of-array/

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans = []

        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans


class Solution(object):
    def getConcatenation(self, nums):
        ans = [0] * 2(len(nums))

        for n in nums:
            ans[n] = nums[n]
            ans[n + len(nums)] = nums[n]
        return ans