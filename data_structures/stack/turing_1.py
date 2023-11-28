from collections import deque

class Stack:
    def __init__(self):
        self.collection = deque()

    def push(self, val):
        self.collection.append(val)

    def pop(self):
        return self.collection.pop()

    def __str__(self):
        return f"{self.collection}"

    def peek(self):
        return self.collection[-1]

    def appendLeft(self, element):
        self.collection.appendleft(element)
    
    def items(self):
        return list(self.collection)

def rotate_with_out(array, K):
    #arr = array

    for i in range(K):
        element = array.pop()
        array[0] = element
        
    return array



def rotate_num(array, K):
    stack = Stack() 
    
    arr = []

    for i in range(0, len(array)):
        stack.push(array[i])
    
    for i in range(K):
        element = stack.pop()
        stack.appendLeft(element)
    
    #print(stack)

    return stack.items()

A = [1, 2, 3, 4, 5, 6, 7]
print(rotate_num(array=A, K=3))
#print(rotate_with_out(array=A, K=3))

B = [-1, -100, 3, 99]
print(rotate_num(array=B, K=2))
#print(rotate_with_out(array=B, K=2))
