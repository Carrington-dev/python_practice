def oddNumbers(l, r):
    # Write your code here
    for num in range(l, r+1):
        if num % 2 == 1:
            print(num)

oddNumbers(2, 5)
