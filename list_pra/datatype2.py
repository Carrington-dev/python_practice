N = int(input())
A = [int(x) for x in input().strip().split(' ')]

found = False
for x in range(100,-101,-1) :
    if found :
        if x in A :
            print(x)
            break
    else :
        if x in A :
            found = True