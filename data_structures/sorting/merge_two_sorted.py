def mergeArrays(a, b):
    n1 = len(a)
    n2 = len(b)
    arr3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0
 
    while i < n1 and j < n2:
        if a[i] < b[j]:
            arr3[k] = a[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = b[j]
            k = k + 1
            j = j + 1
 
    while i < n1:
        arr3[k] = a[i]
        k = k + 1
        i = i + 1
 
    while j < n2:
        arr3[k] = b[j]
        k = k + 1
        j = j + 1

    
    return arr3
a = [1, 5, 7, 7]
b = [0, 1, 2, 3]
print(mergeArrays(a, b))