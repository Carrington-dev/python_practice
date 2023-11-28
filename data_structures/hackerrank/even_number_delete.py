class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next



#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

class LinkedList:
    def __init__(self) :
        self.head = None

    def append(self, newNode):
        if self.head is None:
            self.head = newNode
            
        else:
            current = self.head
            while True:
                if current.next == None:
                    break
                current = current.next
            
            current.next = newNode
    
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
        print(a)
        return a
        """
        def print(self):
                list_rep = ""
                current = self.head
                while True:
                    if list_rep == "":
                        list_rep += f"{current.data}"
                    else:
                        list_rep += f"-->{current.data}"
                    current = current.next

                # print(list_rep)
                if self.head == None:
                    list_rep += "The linked list has no elements"
                return list_rep
                """
    def deleteNode(self, node):
        if self.head == node:
            if self.head.next:
                self.head = self.head.next
        else:
            current = self.head
            previous = self.head
            while True:
                if current.next == None or current == node:
                    break
                previous = current
                current = current.next
            
            previous.next = current.next
    
    # def deleteNodeByValue(self, value):
    #     if self.length() >= 1:
    #         if self.head.data == value:
    #             if self.head.next == None:
    #                 print("List is empty")
    #                 self.head = None
    #             else:
    #                 self.head == self.head.next
    #         else:
    #             current = self.head
    #             previous = self.head
    #             while True:
    #                 if current.next == None:
    #                     break
    #                 if current.data == value:
    #                     current = current
    #                 previous = current
    #                 current = current.next
                
    #             previous.next = current.next

    #     else:
    #         print("the list is empty")


    # def deleteNodeByValue(self, value):
    #     temp = self.head

    #     if (temp != None and temp.data == value):
    #         self.head == temp.next
    #         return

    #     prev = temp
    #     while (temp != None and temp.data != key):
    #         

    #         prev = temp
    #         temp = temp.next

    #     prev.next = temp.next
    

    def deleteNodeByValue(self, key):
        temp = self.head
 
        # If head node itself holds
        # the key to be deleted.
        if(temp != None and temp.data == key):
 
            # Changing head of list.
            self.head = temp.next
            return
 
        # Search for the key to be
        # deleted, keep track of the
        # previous node as we need
        # to change prev.next
        while(temp != None and temp.data != key):
            prev = temp
            temp = temp.next
 
        # If is not present in list
        if(temp == None):
            return
 
        # Unlink the node from
        # linked list
        prev.next = temp.next
        

    
    def length(self):
        lens = 0
        current = self.head
        while True:
            if current.next == None:
                break
            current = current.next
            lens += 1

        return lens
                

# def deleteEven(listHead):
#     # Write your code here
#     current = listHead
#     while current.next:
#         if current.next.data % 2 == 0:
#             current.next = current.next.next
#         current = current.next

#     current = listHead
#     while current.next:
#         print(current.data)
#         current = current.next



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

llinked = LinkedList()

llinked.insert(a)
llinked.insert(b)
llinked.insert(c)
llinked.insert(d)
llinked.insert(e)
llinked.insert(f)

llinked.print()
llinked.deleteNodeByValue(1)
llinked.print()
llinked.deleteNodeByValue(2)
llinked.print()
llinked.deleteNodeByValue(5)
llinked.print()
llinked.deleteNode(f)
llinked.print()