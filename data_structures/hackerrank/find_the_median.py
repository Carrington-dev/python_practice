import math

def findMedian(arr):
    # Write your code here
    n = len(arr)

    arr = sorted(arr) #O(n)

    med = int(math.ceil(n/2))

    # print(med)
    median = arr[med-1]

    # print(arr)
    return median


list1 = [1, 7, 2,5,1]

a = findMedian(list1)
print(a)