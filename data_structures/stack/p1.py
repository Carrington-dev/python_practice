from collections import deque


stack = deque()
print(stack)

stack.append(23)

dir(stack)

print(stack)


class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

    def items(self):
        return self.container


s = Stack()
s.push(23)
s.push(25)
s.push(24)
s.push(27)
s.push(26)

print(s.items())

print(s.size())
