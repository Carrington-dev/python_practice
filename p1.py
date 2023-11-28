number = int(input("Enter a number: "))
factorial = 1

for i in range(0, number+1):
    if i == 0:
        i = 1
        
    factorial *= i

print(factorial)
    
    
