w = int(input("Enter a number: "))
h = int(input("Enter a number: "))
s = str(input("Enter a charector: "))


for i in range(0, w):
    char = ""
    for j in range(0, h):
        char += " " + s + " "
        
    print(char)
    print("\n")
