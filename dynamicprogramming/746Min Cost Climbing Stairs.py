
#bottom up dp tabulation
class Solution(object):
    def minCostClimbingStairs(self, cost):
    
        n = let(cost)
        
        #n + 1 because you need to escape the end 
        dp = [0] * n + 1
        
        #make array and fill in with min values
        dp[i] = min(cost(i - 2) + dp[i - 2], cost[i - 1], dp[i - 1])
        
        #n is the final escaped stair 
        return dp[n]
     




# class Solution(object):
#     def minCostClimbingStairs(self, cost):
        
#     #how many steps
#         n = len(cost)
        
#         #first movement to index 1 is 0 cost
#         memo ={0:0, 1:0}
        
#         def min_cost(i):
#             if i in memo:
#                 return memo[i]
            
#             #check the recursive cost + my last step cost to reach current
#             else: memo[i] = min(cost[i - 2] + min_cost(i - 2),
#                                 cost[i - 1] + min_cost(i - 1))
#             return memo[i]
            
#         return min_cost(n)
    
    
