x = int

def primeNumber(x):
    flag = False
    for i in range(2, x):
        if x%2 == 0:
            flag = True
            break

    # check if flag is True
    if flag:
        print(x, "is not a prime number")
    else:
        print(x, "is a prime number")

while True:
    x = int(input("Enter a number: "))

    if x == 0 or "":
        break

    primeNumber(x)
