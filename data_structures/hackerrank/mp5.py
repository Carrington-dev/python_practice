def miniMaxSum(arr):
    # Write your code here
    #lst = map(int, input().strip().split(' '))
    x = sum(arr)
    print (x-(max(arr))), (x-(min(arr)))



miniMaxSum([10, 5, 21, 1, 17])