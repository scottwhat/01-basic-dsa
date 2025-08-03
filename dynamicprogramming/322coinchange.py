# https://leetcode.com/problems/coin-change/description/
function coinChange(coins []int, amount int) int {
    // Initialize a dp array with size amount + 1, filled with a large value (amount + 1)
    dp := make([]int, amount+1) 
    for i := range dp {
          dp[i] = amount + 1  
    }       
    
