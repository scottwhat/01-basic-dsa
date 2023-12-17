# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


def targetSum(nums, target):
    L, R = 0, len(nums) - 1
    
    while L < R:
        if nums[L] + nums[R] > target:
            R -= 1
            
        elif nums[L] + nums[R] < target:
            L += 1
            
        else:
            return [L, R]

#java 

# class Solution {

#     public int[] twoSum(int[] numbers, int target) {
#         int a_pointer = 0;
#         int b_pointer = numbers.length - 1;
#         int num_a, num_b;

#         while (a_pointer < b_pointer) {
#             num_a = numbers[a_pointer];
#             num_b = numbers[b_pointer];

#             if (num_a + num_b == target) break;

#             if (num_a + num_b < target) {
#                 a_pointer++;
#                 continue;
#             }

#             b_pointer--;
#         }

#         return new int[] { a_pointer + 1, b_pointer + 1 };
#     }
# }