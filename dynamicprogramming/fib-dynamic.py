def memoization(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)
    return cache[n]



#non-recursive - true dynamic
def dp(n):
    if n < 2:
        return n
    
    dp = [0,1]
    i = 2
    
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1
    return dp[1]

print(dp(10))
        



print(memoization(10, {}))