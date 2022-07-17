class Queue:
    def __init__(self, queue_list=[]):
        self.queue = queue_list

    def __str__(self):
        if not self.queue:
            return "queue is empty"
        val_list = [str(x) for x in self.queue]
        return ",".join(val_list)

    def isEmpty(self):
        if not self.queue:
            return True
        else:
            return False

    def enqueue(self,val):
        self.queue.append(val)

    def dequeue(self):
        if self.isEmpty():
            return None
        val = self.queue.pop(0)
        return val

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.queue[0]

    def delete_queue(self):
        self.queue = None


# q = Queue()
# print(q.isEmpty())
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q)
# print(q.dequeue())
# print(q)
# print(q.peek())
# print(q.dequeue())
# q.delete_queue()
# print(q)
#

