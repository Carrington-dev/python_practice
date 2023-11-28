
def solution(A):
    my_array = [i for i in A]
    sum_of_array = 0
    counter = 0

    for i in A:
        sum_of_array += i
   

    # print(sum_of_array)

    maximum = max(my_array)
    half_of_pollution = sum(my_array) / 2
    position = my_array.index(maximum)
    
    while sum(my_array) > half_of_pollution:
        counter += 1
        my_array[position] = maximum /2


    

    return counter

print(solution([5, 19, 8, 1]))
print(solution([10, 10]))
print(solution([3, 0, 5]))