"""
Create a data structure twoStacks that represents two stacks. Implementation of twoStacks should use only one array, i.e., both stacks should use the same array for storing elements. Following functions must be supported by twoStacks.
push1(int x) –> pushes x to first stack
push2(int x) –> pushes x to second stack
pop1() –> pops an element from first stack and return the popped element
pop2() –> pops an element from second stack and return the popped element
Implementation of twoStack should be space efficient.
"""

class TwoStack():
    def __init__(self,maxsize):
        self.two_stack = [None]*maxsize
        self.size = maxsize
        self.top1 = -1
        self.top2 = maxsize

    def push_stack1(self,num):
        if self.top2 - self.top1 > 1:
            self.two_stack[self.top1+1] = num
            self.top1 += 1

    def push_stack2(self,num):
        if self.top2 - self.top1 > 1:
            self.two_stack[self.top2-1] = num
            self.top2 -= 1

    def pop_stack1(self) -> int:
        if self.top1 > -1:
            element = self.two_stack[self.top1]
            self.top1 -= 1
        else:
            element = -1
        return element

    def pop_stack2(self) -> int:
        if self.top2 < self.size:
            element  =self.two_stack[self.top2]
            self.top2 += 1
        else:
            element = -1
        return element

    # def is_empty_stack1(self):
    #     if self.top1 == -1:
    #         return True
    #     else:
    #         return False
    #
    # def is_empty_stack2(self):
    #     if self.top2 == self.size:
    #         return True
    #     else:
    #         return False

    def peek_stack1(self):
        if self.is_empty_stack1():
            return
        else:
            return self.two_stack[self.top1]

    def peek_stack2(self):
        if self.is_empty_stack2():
            return
        else:
            return self.two_stack[self.top2]


two_stack_obj = TwoStack(10)
two_stack_obj.push_stack1(1)
two_stack_obj.push_stack1(2)
two_stack_obj.push_stack1(3)
print(two_stack_obj.peek_stack2())
print(two_stack_obj.peek_stack1())
two_stack_obj.push_stack2(11)
print(two_stack_obj.pop_stack1())
print(two_stack_obj.peek_stack2())
print(two_stack_obj.is_empty_stack1())
print(two_stack_obj.is_empty_stack2())


