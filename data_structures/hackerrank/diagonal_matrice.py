def diagonalDifference(arr):
    # Write your code here
    to_right = 0
    to_left = 0
    n = len(arr)

    for i in range(len(arr)):
        to_right += arr[i][i]
        to_left  += arr[i][n-i-1]
    

    return abs(to_right - to_left)


ar = [
    [1, 2, 3],
    [3, 6, 7],
    [5, 8, 2],
]


diagonalDifference(ar)