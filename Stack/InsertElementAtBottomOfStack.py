"""
Given a stack S and an integer N, the task is to insert N at the bottom of the stack.

Examples:

Input: N = 7
S = 1 <- (Top)
      2
     3
     4
     5
Output: 1 2 3 4 5 7

Input: N = 17
S = 1 <- (Top)
     12
     34
     47
     15
Output: 1 12 34 47 15 17
"""
from StackUsingList import Stack


def insert_at_bottom(stack,num):
    if len(stack) == 0:
        stack.append(num)
    else:
        x = stack.pop()

        insert_at_bottom(stack,num)

        stack.append(x)

        return stack

stack_obj = Stack(5)
stack_obj.push(1)
stack_obj.push(2)
stack_obj.push(3)
stack_obj.push(4)
print(insert_at_bottom(stack_obj.stack,7))