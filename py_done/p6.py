def numPrinter(n):
    numbers = list(range(1,n+1))
    string = ''
    for i in numbers:
        string += str(i)
    print(string) 

if __name__ == '__main__':
    n = int(input())
    numPrinter(n)