from dataclasses import dataclass


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            previous = current
            while current is not None:
                previous = current
                current = current.next
            previous.next = newNode
    
    def insertAt(self, newNode, position):
        
        if position == 0:
            self.append(newNode)
            return
            # newNode.next = head
        elif position < 0 or position > self.listLength():
            print("Invalid position!")
        
        else:
            current = self.head
            count = 1
            while current != None and count < position:
                current = current.next
                count += 1
            
            prev_next = current.next
            current.next = newNode
            newNode.next = prev_next
                
           
            # newNode.next = prev.next
    
    def listLength(self):
        length = 0
        current = self.head
        
        while current is not None:
            length += 1
            current = current.next
        # print(length)
        return length
    
    def deleteNode(self, oldNode):
        if self.head == oldNode:
            self.head = self.head.next
            return
        else:
            current = self.head
            previous = current
            while current != None and current != oldNode:
                previous = current
                current = current.next
            
            previous.next = current.next


    def deleteAt(self, position):
        if position == 0:
            self.deleteNode(self.head)
        elif position < 0 or position > self.listLength():
            print("Invalid position")
        else:
            current = self.head
            previous = current
            count = 0
            while current != None:
                if position == count:
                    previous.next = current.next


                previous = current
                current = current.next
                count += 1
            
            # previous.next = current.next
            # self.deleteNode(current)
    
    def printMe(self):
        a = ""
        current = self.head
        while current is not None:
            if a == "":
                a += f"{current.data}"
            else:
                a += f" --> {current.data}"
            current = current.next
        
        print(a)
    

    def searchNode(self, nodeValue):
        searchedNode = None
        current = self.head
        while current != None and current.data != nodeValue:
            current = current.next
        searchedNode = current
        return searchedNode
    
    def reverseLinkedList(self):
        # 1-> 2 -> 3 -> 4 | 4 -> 3 -> 2 -> 1 
        current = self.head
        previous = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            
            current = next
        self.head = previous
    
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        
    

    
a = Node(2)
b = Node(3)
c = Node(1)
d = Node(4)
e = Node(5)

myLinkedList = LinkedList()
myLinkedList.append(a)
myLinkedList.append(b)
myLinkedList.append(c)
myLinkedList.insertAt(d, 2)
myLinkedList.insertAt(e, 3)
myLinkedList.printMe()
myLinkedList.reverseLinkedList()
# lL = myLinkedList.listLength()

# print(lL)
# myLinkedList.deleteNode(c)
# myLinkedList.deleteAt(2)
# myLinkedList.deleteAt(0)
myLinkedList.printMe()
myLinkedList.reverseLinkedList()
myLinkedList.printMe()
# d5 = myLinkedList.searchNode(5)
# print(d5.data)

"""
1. append a node at the first position
2. append a node in between 2 nodes given a node and a position
3. append a node at the end of the list
4. delete a node
5. delete a node by value
6. deleting a node with even or odd values


Todo
a. Search a node by value
b. reverse a linked list

a. Learn about a doubly linked list

"""