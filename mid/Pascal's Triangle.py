def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    triangle = list()
    
    if numRows == 0:
        return triangle

    triangle.append([1])
    
    for i in range(1, numRows):
        cur_triangle = []
        pre_triangle = triangle[i - 1]

        cur_triangle.append(1)

        for j in range(1, i):
            cur_triangle.append(pre_triangle[j] + pre_triangle[j - 1])

        cur_triangle.append(1)

        triangle.append(cur_triangle)

    return triangle    


print(generate(5))