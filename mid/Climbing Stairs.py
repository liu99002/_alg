def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2:
        return n
    
    dp = [None] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

print(climbStairs(10))