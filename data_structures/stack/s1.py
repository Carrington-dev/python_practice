from collections import deque

#s = deque()
#print(s)

class Stack:
    def __init__(self):
        self.container = deque()


    def pop(self):
        return self.container.pop()

    def push(self, value):
        return self.container.append(value)

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def __str__(self):
        return f"{list(self.container)}"

def reverse_string(string):
    stack = Stack()

    for char in string:
        stack.push(char)


    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    print(stack)

    return rev_str


if __name__ == '__main__':
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am the king"))
    print(reverse_string("Carrington Muleya"))

    print(reverse_string(reverse_string("Carrington Muleya")))
    



s = Stack()
s.push(23)

print(s.is_empty())
print(s)
print(s.size())




