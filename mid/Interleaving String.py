import numpy as np
def isInterleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    dp = np.zeros([len(s2) + 1, len(s1) + 1])
    

    if len(s3) != len(s1) + len(s2):
        return 0

    for i in range(0, len(s1) + 1):
        for j in range(0, len(s2) + 1):
            if i == 0 and j == 0:
                dp[0][0] = 1
            elif i == 0:
                if dp[j - 1][i] == 1 and s3[i + j - 1] == s2[j - 1]:
                    dp[j][i] = 1
            elif j == 0:
                if dp[j][i - 1] == 1 and s3[i + j - 1] == s1[i - 1]:
                    dp[j][i] = 1
            else : 
                if dp[j - 1][i] == 1 and s3[i + j - 1] == s2[j - 1] or dp[j][i - 1] == 1 and s3[i + j - 1] == s1[i - 1]:
                    dp[j][i] = 1
    return dp[len(s2)][len(s1)]

s1 = "aabcc" 
s2 = "dbbca" 
s3 = "aadbbbaccc"

print(isInterleave(s1, s2, s3))