def hasValidPath(grid):
    """
    :type grid: List[List[str]]
    :rtype: bool
    """
    m, n = len(grid), len(grid[0])  
    max_balance = m + n

    dp = [[set() for _ in range(n)] for __ in range(m)]  
    
    for i in range(m):  
        for j in range(n):  
            if i == 0 and j == 0:
                if grid[i][j] == '(':  
                    dp[i][j].add(1)  
                elif grid[i][j] == ')':   
                    return False
            elif i == 0 :
                for balance in dp[i][j - 1]:
                    char = grid[i][j]
                    if char == '(':  
                        new_balance = balance + 1  
                        if new_balance <= max_balance:  
                            dp[i][j].add(new_balance)  
                    elif char == ')':  
                        new_balance = balance - 1  
                        if new_balance >= 0:  
                            dp[i][j].add(new_balance)
            elif j == 0:
                for balance in dp[i - 1][j]:
                    char = grid[i][j]
                    if char == '(':  
                        new_balance = balance + 1  
                        if new_balance <= max_balance:  
                            dp[i][j].add(new_balance)  
                    elif char == ')':  
                        new_balance = balance - 1  
                        if new_balance >= 0:  
                            dp[i][j].add(new_balance)
            else:
                for balance in dp[i - 1][j]:   
                    char = grid[i][j]
                    if char == '(':  
                        new_balance = balance + 1  
                        if new_balance <= max_balance:  
                            dp[i][j].add(new_balance)  
                    elif char == ')':  
                        new_balance = balance - 1  
                        if new_balance >= 0:  
                            dp[i][j].add(new_balance)
                for balance in dp[i][j - 1]:   
                    char = grid[i][j]
                    if char == '(':  
                        new_balance = balance + 1  
                        if new_balance <= max_balance:  
                            dp[i][j].add(new_balance)  
                    elif char == ')':  
                        new_balance = balance - 1  
                        if new_balance >= 0:  
                            dp[i][j].add(new_balance)
    return 0 in dp[m - 1][n - 1]  