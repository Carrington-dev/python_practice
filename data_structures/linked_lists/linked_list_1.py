from os import link
import re


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"{self.data}"
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            # pass
            lastNode = self.head
            while True:
                if lastNode.next == None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def appendLeft(self, newHead):
        tmp = self.head

        if tmp:
            self.head = newHead
            self.head.next = tmp
        else:
            self.head = newHead
        
    
    def print(self):
        a = ""
        current = self.head
        while current:
            if a != "":
                a += f"-->{current.data}"
            else:
                a += f"{current.data}"
            current = current.next

        if self.head == None:
            a += "The linked list has no elements"
        
        return a

    def length(self):
        a = 0
        node = self.head
        while node:
            a += 1
            node = node.next
        
        return a

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(0)

linked_list = LinkedList()

linked_list.insert(a)
linked_list.insert(b)
linked_list.insert(c)
linked_list.insert(d)
linked_list.insert(e)
linked_list.insert(f)
linked_list.appendLeft(g)
print(linked_list.length())
print(linked_list.print())