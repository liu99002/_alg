import numpy as np
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    boolarray = np.zeros((len(s), len(s))) 
    Palindrome = ""

    #s = 1
    for i in range(0, len(s)):
        boolarray[i][i] = 1
        if len(s[i]) > len(Palindrome):
            Palindrome = s[i]

    #s = 2 
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:    
            boolarray[i][i + 1] = 1
            if len(s[i] + s[i + 1]) > len(Palindrome):
                Palindrome = s[i] + s[i + 1]
    
    #s > 3
    for j in range(2, len(s)):
        for i in range(0, len(s) - 2):
            if s[i] == s[j] and boolarray[i + 1][j - 1] == 1:
                boolarray[i][j] = 1
                if len(s[i:j + 1]) > len(Palindrome):
                    Palindrome = s[i:j + 1]
    return Palindrome
s = "cbbdad"
print(longestPalindrome(s))