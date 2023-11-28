def insertion_sort(elements):
    for i in range(1, len(elements)):
        current_element = elements[i]
        pos = i

        while current_element < elements[i-1] and pos > 0:
            elements[pos] = elements[pos - 1]
            pos = pos - 1
        elements[pos] = current_element


list1 = [2, 4, 3, 6, 1]
insertion_sort(elements=list1)
print(list1)
