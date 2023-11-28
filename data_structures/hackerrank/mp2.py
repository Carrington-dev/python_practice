def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    left = 0
    right = 0

    for i in range(n):
        #print("i = ", str(i))
        left += arr[i][i]
        right += arr[i][n-i-1]
    
    #print(left, right)

    return abs(left - right)


diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])

