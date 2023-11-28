def sortelementst(elements):
    size = len(elements)

    for i in range(size - 1):
        visited  = False
        for j in range(size - 1):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[ j + 1]
                elements[j+1] = tmp

                visited = True
        
        if not visited:
            break
    
    return elements


elements = [23, 67, 2, 1, 0, -3]
print(sortelementst(elements))