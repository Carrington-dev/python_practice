def rotateLeft(d, arr):
    # Write your code here
    new_list = []
    
    for i in range(d):
        new_list.append(arr.pop(0))
    
    
    arr += new_list
    # print(new_list)
    # print(arr)

    return arr

arr = [ 1, 2, 3, 4, 5]

rotateLeft(2, arr)