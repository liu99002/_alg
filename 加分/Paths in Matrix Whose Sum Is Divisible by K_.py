
def hasValidPath(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: bool
    """
    m, n = len(grid), len(grid[0])  
    max_balance = m + n

    dp = [[set() for _ in range(n)] for __ in range(m)]  
    
    if grid[0][0] == '(':  
        dp[0][0].add(1)  
    elif grid[0][0] == ')':  
        return False

    for i in range(m):  
        for j in range(n):  
            for balance in dp[i][j]:  
                if j + 1 < n:  
                    char = grid[i][j + 1]  
                    if char == '(':  
                        new_balance = balance + 1  
                        if new_balance <= max_balance:  
                            dp[i][j + 1].add(new_balance)  
                    elif char == ')':  
                        new_balance = balance - 1  
                        if new_balance >= 0:  
                            dp[i][j + 1].add(new_balance)  
                if i + 1 < m:  
                    char = grid[i + 1][j]  
                    if char == '(':  
                        new_balance = balance + 1  
                        if new_balance <= max_balance:  
                            dp[i + 1][j].add(new_balance)  
                    elif char == ')':  
                        new_balance = balance - 1  
                        if new_balance >= 0:  
                            dp[i + 1][j].add(new_balance)  
    return 0 in dp[m - 1][n - 1]   