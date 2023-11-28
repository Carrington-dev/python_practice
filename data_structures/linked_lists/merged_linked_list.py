from linked_list2 import LinkedList, Node

def mergeLinkedList(firstList, secondList, mergedList):
    currentFirst = firstList.head
    currentSecond = secondList.head

    while True:
        if currentFirst is None:
            mergedList.append(currentSecond)
            break
        if currentSecond is None:
            mergedList.append(currentFirst)
            break
        if currentFirst.data < currentSecond.data:
            currentFirstNext = currentFirst.next
            currentFirst.next = None
            mergedList.append(currentFirst)
            currentFirst = currentFirstNext
        else:
            currentSecondNext = currentSecond.next
            currentSecond.next = None
            mergedList.append(currentSecond)
            currentSecond = currentSecondNext

firstList = LinkedList()
secondList = LinkedList()
mergedList = LinkedList()

a = Node(1)
b = Node(5)
c = Node(9)

firstList.append(a)
firstList.append(b)
firstList.append(c)

d = Node(2)
e = Node(4)
f = Node(8)
g = Node(10)

secondList.append(d)
secondList.append(e)
secondList.append(f)
secondList.append(g)

myResults = mergeLinkedList(firstList, secondList, mergedList)
# myResults
mergedList.printMe()