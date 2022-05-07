"""
Implement stack methods: push(),pop(),is_empty(),peek() with list data structure
Also implement Stack overflow and stack underflow operations.
"""


class StackUnderflowError:
    pass


class Stack:
    def __init__(self,max_size):
        self.stack = []
        self.max_size = max_size
        self.top = -1

    def push(self,num):
        if self.is_full():
            raise OverflowError('StackOverflowError')
        else:
            self.stack.append(num)
            self.top += 1

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError('Stack underflow')
        else:
            num = self.stack.pop()
            self.top -= 1
            return num

    def is_full(self):
        if len(self.stack) == self.max_size:
            return True
        else:
            return False

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError('Stack underflow')
        else:
            return self.stack[-1]


stack_obj = Stack(5)
stack_obj.push(1)
stack_obj.push(2)
print(stack_obj.pop())
stack_obj.push(3)
stack_obj.push(4)
print(stack_obj.peek())
stack_obj.push(5)
stack_obj.push(6)
print(stack_obj.pop())
print(stack_obj.pop())
print(stack_obj.pop())
print(stack_obj.pop())
print(stack_obj.pop())
print(stack_obj.pop())


