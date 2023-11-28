def find_sum_of_two(A, val):
    #TODO: Write - Your - Code
    booll = False
    for i in A:
        if val -i in A:
            booll = True
    return booll

print(find_sum_of_two([12, 56, 67],45))
print(find_sum_of_two([12, 3, 56, 67],15))
