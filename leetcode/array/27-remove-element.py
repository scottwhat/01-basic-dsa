class Solution(object):
    def removeElement(self, nums, val):

        # move along the array and if theres a undesired value swap it with the next desired value

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        # return the length of valid nums

        return k
