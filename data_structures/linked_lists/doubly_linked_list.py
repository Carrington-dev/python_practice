class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current != None:
                prev = current
                # current.prev = prev
                current = current.next
            # current.
            newNode.prev = prev
            prev.next = newNode
    
    def findLastNode(self):
        lastNode = None
        if self.head == None:
            return lastNode
        else:
            current = self.head
            while current != None:
                prev = current
                current = current.next
            lastNode = prev
        # print(lastNode.data)
        return lastNode
    
    def printBack(self):
        a = ""
        if self.findLastNode() == None:
            return a
        else:
            last = self.findLastNode()
            while last is not None:
                # print(last.data)
                if a == "":
                    a  += f"{last.data}"
                else:
                    a += f"-->{last.data}"
                last = last.prev
        print(a)
        return a
    
    def printNode(self):
        a = ""
        if self.head is None:
            a = "Empty list"
        else:
            current = self.head
            while current is not None:
                if a == "":
                    a += f"{current.data}"
                    
                else:
                    a += f"-->{current.data}"
                current = current.next
        print(a)
        return a
        
a = Node(2)
b = Node(3)
c = Node(1)
d = Node(4)
e = Node(5)

myLinkedList = LinkedList()
myLinkedList.append(a)
myLinkedList.append(b)
myLinkedList.append(c)
myLinkedList.append(d)
myLinkedList.append(e)
myLinkedList.printNode()
myLinkedList.printBack()