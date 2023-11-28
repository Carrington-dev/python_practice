def maxNum(array, k):
    sum = 0
    #"""
    for i in array:
        for j in array:
            s = i + j
            if sum < s and s < k:
                sum = s
    #"""
    """
    arr = [ i + j for i in array for j in array if (i+j) < k]
    print(arr)

    for num in arr:
        if num > sum and num < k:
            sum = num
    """
    if sum == 0:
        return -1
    
    return sum

A = [34, 23, 1, 24, 75, 33, 54, 8]
k = 60

print(maxNum(A, k))


B = [10, 20, 30]
m = 15

print(maxNum(A, m))