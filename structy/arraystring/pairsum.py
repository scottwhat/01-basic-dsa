def pair_sum(numbers, target_sum):
  #target sum 
  #return a tuple (,) with a pair that hits target 

  previous_nums = {}

  for index, num in enumerate(numbers):
    complement = target_sum - num

    if complement in previous_nums:
      return (index, previous_nums[complement])

    previous_nums[num] = index