
def factorial(n):
    if n==1 or n==0:
        n = 1
    else:
        n= n * factorial(n-1)
    return n

while True:
    num = int(input("Enter a number "))
    if num == -1:
        break
    print(factorial(num))
    
