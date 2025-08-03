# https://leetcode.com/problems/climbing-stairs/description/


#bottom up constant space 2 variables 
class Solution(object):
    def climbStairs(self, n): 

        if n == 1:
            return 1

        if n == 2:
            return 2

        prev = 1
        cur = 2

        for i in range(2, n):
            prev, cur = cur, prev + cur
        
        return cur

# bottom up tabulation
# class Solution(object):
#     def climbStairs(self, n): 

#         if n == 1:
#             return 1

#         if n == 2:
#             return 2

#         dp = [0] * n
#         dp[0] = 1
#         dp[1] = 2

#         for i in range(2, n):
#             dp[i] = dp[i - 2] + dp[i - 1]
        
#         return dp[n - 1]

#top down memo
# class Solution(object):
#     def climbStairs(self, n): 

#         memo = {1:1, 2:2}

#         def recursive_climb(n):
#             if n in memo:
#                 return memo[n]

#             memo[n] = recursive_climb(n - 1) + recursive_climb(n - 2 )
#             return memo[n]

#         return recursive_climb(n)