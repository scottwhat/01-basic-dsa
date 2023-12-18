

# https://leetcode.com/problems/contains-duplicate-ii/

## steps
## Loop 
# first check if window needs to be shifted, R - L   + 1 > k? yes set remove nums[L], shift left pointer +1
# second check if nums[R] in window, true
# window.add(nums[R])


nums = [2,4,3,2,2,3,4]


def closeDuplicates(nums, k):
    window = set() # Cur window of size <= k
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])

    return False



print(closeDuplicates(nums, 2))
