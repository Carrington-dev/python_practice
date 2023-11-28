def merge_sort(arr):
    

    if len(arr) > 1:

        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]


        merge_sort(L)


        merge_sort(R)

        k = i  = j = 0


        while i < len(L)  and j < len(R):

            if L[i] < R[j]:

                arr[k] = L[i]

                i += 1

            else:
                
                arr[k] = R[j]

                j += 1
            
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[i]
            j += 1
            k += 1
   
    #return arr
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
  
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    merge_sort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

"""
if __name__ == '__main__':
    #elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    #quick_sort(elements, 0, len(elements)-1)
    #print(elements)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
        ["mona", "dhaval", "aamir", "tina", "chang"]
    ]

    for elements in tests:
        merge_sort(elements)
        print(f'sorted array: {elements}')
"""