def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[b]


def partition(arr, low, high):
    i = (low -1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:

            i += 1
            arr[j], arr[i] = arr[i], arr[j]
        
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)


a = 2
b = 7


swap(a, b, [2,4])

if __name__ == '__main__':
    #elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    #quick_sort(elements, 0, len(elements)-1)
    #print(elements)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
        ["mona", "dhaval", "aamir", "tina", "chang"]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')
