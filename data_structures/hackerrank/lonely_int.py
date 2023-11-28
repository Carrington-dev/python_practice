def lonelyinteger(a):
    # a = [1, 2, 3, 4, 3, 2, 1]
    # set_a = [ 1, 2, ]
    a = sorted(a)
    
    lonely_int = a[-1]

    print(lonely_int)

a = [1, 2, 3, 4, 3, 2, 1]
lonelyinteger(a)