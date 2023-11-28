def hourglassSum(arr):
    # Write your code here
    """
    [
        [1, 4 , 6, 7, 8, 7],
        [1, 4 , 6, 7, 8, 7],
        [1, 4 , 6, 7, 8, 7],
        [1, 4 , 6, 7, 8, 7],
        [1, 4 , 6, 7, 8, 7],
        [1, 4 , 6, 7, 8, 7],


    ]
    """


    best = 0
    check_negs = False
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j+2 < len(arr) and i + 2 < len(arr):
                hour_glass_sum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
                if sum(arr[i]) > 0:  
                    
                    if best < hour_glass_sum:
                        best = hour_glass_sum
                else:
                    if best > hour_glass_sum:
                        best = hour_glass_sum
                        
    print(best)
    

test_list = [
        [1, 4 , 6, 7, 8, 7],
        [1, 4 , 6, 7, 8, 7],
        [1, 4 , 6, 7, 8, 7],
        [1, 4 , 6, 7, 8, 7],
        [1, 4 , 6, 7, 8, 7],
        [1, 4 , 6, 7, 8, 7],

]

test_2 = [
    [ -9, -9, -9 , 1, 1, 1 ],
    [0 ,-9,  0 , 4, 3, 2],
    [-9 ,-9 ,-9,  1 ,2, 3],
    [0  ,0 , 8 , 6, 6, 0],
    [0 , 0 , 0, -2, 0, 0],
    [0 , 0 , 1 , 2, 4, 0],
]

test_3 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

test_4 = [
    [-1, -1, 0 ,-9 , -2 ,-2],
    [-2, -1, -6, -8,  -2, -5],
    [-1, -1, -1, -2,  -3, -4],
    [-1, -9, -2, -4,  -4, -5],
    [-7, -3, -3, -2,  -9, -9],
    [-1, -3, -1, -2,  -4, -5],
]
hourglassSum(test_2)
hourglassSum(test_list)
hourglassSum(test_3)
hourglassSum(test_4)

s = [-2 , -5]

s = sum(s)

print(s)