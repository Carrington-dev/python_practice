if __name__ == '__main__':
    #n = int(raw_input())
    #integer_list = map(int, raw_input().split())
    
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    n = int(input())
    vals = input().split()
    lst = []
    for i in range (0, n):
        lst.append(int(vals[i]))

    print (hash(tuple(lst)))