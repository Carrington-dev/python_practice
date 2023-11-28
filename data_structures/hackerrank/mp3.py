def plusMinus(arr):
    # Write your code here
    prop_list_1 = [ -1 for i in arr if i < 0  ]
    prop_list_2 = [ 1 for i in arr if i > 0  ]
    prop_list_3 = [ 0 for i in arr if i == 0  ]

    total = len(prop_list_1) + len(prop_list_2) + len(prop_list_3)
    less_1 = len(prop_list_1)
    less_2 = len(prop_list_2)
    less_3 = len(prop_list_3)

    print("{0:.6f}".format(less_1/total))
    print("{0:.6f}".format(less_2/total))
    print("{0:.6f}".format(less_3/total))



arr = [0, -2, 3, -6, 6]

plusMinus(arr)