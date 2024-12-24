def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    dp = [[0] * n for _ in range(m)]
    for i in range(0,m):
        for j in range(0,n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

print(uniquePaths(3,5))