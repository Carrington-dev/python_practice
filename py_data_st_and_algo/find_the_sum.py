def findElement(A, k):
    for i in range(len(A)):
        if A[i] == k:
            return A[i]
    
    return -1


def findSum(A, k):
    context = {i:i for i in A}

    for key in context.keys():
        if context.get(k - key) != None and (k - key) != key:
            return (key, context[(k - key)])
    
    return None
k = 20
B = [12, 6, 8, 9, 20, 45, 23, -3]
print(findSum(B, k))