"""
Write a program to reverse a stack using recursion. You are not allowed to use loop constructs like while, for..etc, and you can only use the following ADT functions on Stack S:
isEmpty(S)
push(S)
pop(S)
"""
from InsertElementAtBottomOfStack import *
from StackUsingList import Stack

def reverse_stack(stack):

    if len(stack) == 1:
        return stack

    x = stack.pop()

    reverse_stack(stack)

    insert_at_bottom(stack,x)

    return stack


stack_obj = Stack(5)
stack_obj.push(1)
stack_obj.push(2)
stack_obj.push(3)
stack_obj.push(4)
print(reverse_stack(stack_obj.stack))
