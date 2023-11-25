
def subsetsWithoutDuplicates(nums):
    subsets = []
    curSet = []
    helper(0, nums, curSet, subsets)
    return subsets


def helper(i, nums, curSet, subsets):
    if i >= len(nums):
        subsets.append(curSet.copy())
        return

        # decision to include nums[i]
    curSet.append(nums[i])
    helper(i + 1, nums, curSet, subsets)
    curSet.pop()

    helper(i + 1, nums, curSet, subsets)


print(subsetsWithoutDuplicates([1, 2, 3]))
