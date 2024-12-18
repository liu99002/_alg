def numTrees(n):
    """
    :type n: int
    :rtype: int
    """
    numstree = list()
    numstree.append(1)
    numstree.append(1)

    for i in range(2, n + 1):
        nums = 0
        for j in range(0, i):
            nums += numstree[j] * numstree[i - j - 1]
        numstree.append(nums)
    return numstree[n]

print(numTrees(3))