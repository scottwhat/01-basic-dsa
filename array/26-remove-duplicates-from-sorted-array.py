class Solution(object):
    def removeDuplicates(self, nums):
        # use two pointers, left stays as the recent unique element
        # right pointer searches for next

        left_pointer = 1
        for right_pointer in range(1, len(nums)):
            if nums[right_pointer] != nums[right_pointer - 1]:
                nums[left_pointer] = nums[right_pointer]
                left_pointer += 1

        return left_pointer

