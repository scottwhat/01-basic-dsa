def non_adjacent_sum(nums):
  return _non_adjacent_sum(nums, 0, {})

def _non_adjacent_sum(nums, i, memo):
  if i in memo:
    return memo[i]
  
  if i >= len(nums):
    return 0
  
  include = nums[i] + _non_adjacent_sum(nums, i + 2, memo)
  exclude = _non_adjacent_sum(nums, i + 1, memo)
  memo[i] = max(include, exclude)
  return memo[i]


def non_adjacent_sum(nums):
    if not nums:
        return 0
    return max(nums[0] + non_adjacent_sum(nums[2:]), non_adjacent_sum(nums[1:]))

def non_adjacent_sum(nums):
        memo = {}
        def helper(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            include = nums[i] + helper(i + 2)
            exclude = helper(i + 1)
            memo[i] = max(include, exclude)
            return memo[i]
        
        return helper(0)