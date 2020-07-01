

class Node:
    def __init__(self, data, nextElm=None):
        self.data = data
        self.next = nextElm

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

    def getData(self):
        return self.data

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.size = 1

    def insertLast(self, data):
        newNode = Node(data)
        self.tail.setNext(newNode)
        self.tail = newNode
        self.size += 1

    def insertFirst(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1

    def removeHead(self):
        if self.size != 1:
            self.head = self.head.getNext()
            self.size -= 1

    def removeTail(self):
        current = self.head
        previous = self.head

        while current.getNext() != None:
            previous = current
            current = current.getNext()
        
        previous.setNext(None)
        self.size -= 1

    def getMidpoint(self):

        if self.size == 2:
            return self.head

        slow = self.head
        fast = self.head
        while fast.getNext() != None and fast.getNext().getNext() != None:
            slow = slow.getNext()
            fast = fast.getNext().getNext()

        return slow

    def length(self):
        return self.size

    def __str__(self):
        current = self.head
        string = ''
        while current != None:
            string += ' ' + str(current.getData())
            current = current.getNext()

        return string

testList = LinkedList(2)
print(testList, "Initial")

testList.insertFirst(3)
print(testList, "Head Insertion")

testList.insertLast(5)
print(testList, "Tail Insertion")

print(testList.getMidpoint().getData(), "Get Midpoint")

testList.removeHead()
print(testList, "Head Removal")

testList.removeTail()
print(testList, "Tail Removal")

print(testList.length(), "Size")
