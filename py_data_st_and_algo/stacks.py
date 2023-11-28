#FIFO queques
#LIFO stacks
from collections import deque

    

class Queue:
    def __init__(self):
        self.children = deque()
    
    def enqueue(self, x):
        self.children.appendleft(x)
    
    def dequeue(self):
        return self.children.pop()
    
    def print(self):
        n = len(self.children)
        print(self.children[n-1])
    
    
