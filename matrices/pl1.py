from typing import Sequence


# map(function, sequence)
num_list = [ 0 for i in range(9)]
print(num_list)

for i in range(9):
    num_list[i] = int(input(f"Enter item {i} on the list: "))


print(num_list)