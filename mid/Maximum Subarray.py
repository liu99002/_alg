def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxnums = list()
    maxnums.append(nums[0])

    for i in range(1, len(nums)):
        maxnums.append(max(maxnums[i - 1] + nums[i], nums[i]))
    return max(maxnums)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))