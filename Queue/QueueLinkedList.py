class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return ' '.join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        return False

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.LinkedList.head

    def enqueue(self,value):
        node = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = node
            self.LinkedList.tail = node
        else:
            self.LinkedList.tail.next = node
            self.LinkedList.tail = node

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            tempNode = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
            return tempNode

    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None


customQ = Queue()
print(customQ.isEmpty())
customQ.enqueue(1)
customQ.enqueue(2)
customQ.enqueue(3)
print(customQ)
print(customQ.peek())
print(customQ.dequeue())
print(customQ.peek())
customQ.delete()
print(customQ.peek())

