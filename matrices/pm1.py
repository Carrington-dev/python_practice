matric = [[0 for i in range(4)] for j in range(4)]
print(matric)

for i in range(4):
    for j in range(4):
        matric[i][j] = int(input(f"Enter item {i+1} {j+1} on the list: "))


print(matric)