

def sum(m, n):
    s = m
    if m == n:
        return s
    else:
        return s + sum(m+1,n)

while True:
    m = int(input("Enter a number m "))
    n = int(input("Enter a number n "))
    if m > n:
        print("m must be less than n")
    else:
        print(sum(m,n))

