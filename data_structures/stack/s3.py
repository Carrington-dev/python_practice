from collections import deque

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
        #return f"{self.container}"

def reverse_string(string):
    stack = Stack()
    list_of_splitted_words = string.split(" ")

    for char in list_of_splitted_words:
        stack.push(char)


    rev_str = []
    while not stack.is_empty():
        rev_str.append( stack.pop() )

    joined = " ".join(rev_str)


    return joined


if __name__ == '__main__':
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am the king "))
    print(reverse_string("Carrington Muleya "))
    print(reverse_string("Hello World "))

    #print(reverse_string(reverse_string("Carrington Muleya")))

    
"""
def reverse_word(string):

    reserved_string = []

    stack = Stack()

    for i in string.split():
        stack.push(i)

    print(stack)

    while not stack.is_empty:
        #print(stack.pop())
        reserved_string.append(stack.pop())

    print(stack)

    strings = " ".join(reserved_string)
    

    return string

txt = "welcome to the jungle"

a = reverse_word(txt)
print(a)"""

    
    
    

