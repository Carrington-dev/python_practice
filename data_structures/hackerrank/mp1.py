
import os

def compareTriplets(a, b):
    # Write your code here
    aa = 0
    bb = 0
    
    for i in range(len(a)):
        if a[i] > b[i]:
            aa += 1
        elif a[i] < b[i]:
            bb += 1
        else:
            pass
    
    return ( aa, bb)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

   # fptr.close()
