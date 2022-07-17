"""
Write code to reverse a queue.
Time complexity: O(n)
space complexity: O(n)

Approach1:
Using stack:
i) pop elements from queue one by one and insert in the stack until queue is empty.
ii) pop elements from stack oe by one and insert in the queue until stack is empty.

Approach2:
using recursion:
i) pop the current element
ii) reverse the left queue
iii) append the popped element to the end
Using Recursion:

"""
from Queue import Queue
from Stack.StackUsingList import Stack

def reverse_queue_approach1(q):
    s = Stack(5)
    while not q.isEmpty():
        s.push(q.peek())
        q.dequeue()

    while not s.is_empty():
        q.enqueue(s.peek())
        s.pop()

    print("reverse queue=",q)

def reverse_queue_approach2(q):
    if q.isEmpty():
        return
    else:
        x = q.peek()
        q.dequeue()
        reverse_queue_approach2(q)
        q.enqueue(x)
        return q




q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
reverse_queue_approach1(q)
print(reverse_queue_approach2(q))