class Queue:
    def __init__(self, maxSize):
        self.queue = maxSize * [None]
        self.maxSize = maxSize
        self.front = -1
        self.rear = -1

    def __str__(self):
        values = [str(x) for x in self.queue if x is not None]
        return ",".join(values)

    def isFull(self):
        if self.rear + 1 == self.front:
            return True
        elif self.rear + 1 == self.maxSize and self.front == 0:
            return True
        else:
            return False

    def isEmpty(self):
        if self.rear == -1:
            return True
        else:
            return False

    def enqueue(self,value):
        if self.isFull():
            return "Queue is full"
        else:
            if self.rear + 1 == self.maxSize:
                self.rear = 0
            else:
                self.rear += 1
                if self.front == -1:
                    self.front = 0
        self.queue[self.rear] = value
        return "element inserted in the queue"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            val = self.queue[self.front]
            front = self.front
            if self.rear + 1 == self.maxSize:
                self.rear = 0
            elif self.rear == self.front:
                self.rear = -1
                self.front = -1
            else:
                self.front += 1
            self.queue[front] = None
            return val

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.queue[self.front]

    def delete_queue(self):
        self.queue = self.maxSize * [None]
        self.front = -1
        self.rear = -1


customQ = Queue(3)
print(customQ.isEmpty())
customQ.enqueue(1)
customQ.enqueue(2)
customQ.enqueue(3)
print(customQ)
print(customQ.dequeue())
print(customQ.peek())
print(customQ)
customQ.delete_queue()
print(customQ.peek())

