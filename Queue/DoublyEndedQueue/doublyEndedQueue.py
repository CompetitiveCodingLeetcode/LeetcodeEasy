"""
input from both ends. push_back(),push_front()

output from both ends. pop_back(),pop_front()

"""

class DoubleEndedQueue():
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.front = -1
        self.rear = -1
        self.queue = [None] * self.maxsize

    def push_back(self,val):
        if self.is_full():
            return "queue is full"
        else:
            #when queue is empty
            if self.is_empty():
                self.front += 1
                self.rear += 1
            #handle cyclic case
            elif self.rear == self.maxsize-1:
                self.rear = 0
            else:
                self.rear += 1
            self.queue[self.rear] = val

    def push_front(self,val):
        if self.is_full():
            return "queue is full"
        else:
            #when queue is empty
            if self.is_empty():
                self.front += 1
                self.rear += 1
            # when there is only one element in queue(cyclic case)
            elif self.front == 0:
                self.front = self.maxsize-1
            else:
                self.front -= 1
            self.queue[self.front] = val

    def pop_back(self):
        if self.is_empty():
            return "queue is empty"
        else:
            val = self.queue[self.rear]
            rear = self.rear
            # handle cyclic case
            if self.front == self.rear:
                self.rear = -1
                self.front = -1
            # when there is one element in queue
            elif self.rear == 0:
                self.rear = self.maxsize-1
            else:
                self.rear -= 1
            self.queue[rear] = None
            return val

    def pop_front(self):
        if self.is_empty():
            return "queue is empty"
        else:
            val = self.queue[self.front]
            front = self.front
            if self.rear == self.front:
                self.rear = -1
                self.front = -1
            # handle cyclic case
            elif self.front + 1 == self.maxsize:
                self.front = 0

            else:
                self.front += 1
            self.queue[front] = None
            return val

    def is_empty(self):
        if self.front == -1:
            return True
        return False

    def is_full(self):
        if self.front == 0 and self.rear == self.maxsize-1:
            return True
        elif self.rear == self.front-1:
            return True
        return False

# deq = DoubleEndedQueue(4)
# print(deq.pop_front())
# print(deq.pop_back())
# print(deq.push_back(1))
# print(deq.push_front(2))
# print(deq.pop_front())
# print(deq.push_back(3))
# print(deq.push_back(4))
# print(deq.push_front(5))
# print(deq.push_back(6))
# print(deq.pop_front())
# print(deq.pop_back())

