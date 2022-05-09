"""
Given a stack, sort it using recursion. Use of any loop constructs like while, for..etc is not allowed. We can only use the following ADT functions on Stack S:

is_empty(S)  : Tests whether stack is empty or not.
push(S)         : Adds new element to the stack.
pop(S)         : Removes top element from the stack.
top(S)         : Returns value of the top element. Note that this
               function does not remove element from the stack.
Example:

Input:  -3  <--- Top
        14
        18
        -5
        30

Output: 30  <--- Top
        18
        14
        -3
        -5
"""
from Stack.StackUsingList import Stack


def sorted_insert(stack,num):
    if len(stack) == 0 or stack[-1] < num:
        stack.append(num)
        return

    x = stack.pop()

    sorted_insert(stack,num)

    stack.append(x)



def sort_stack(stack):
    if len(stack) == 0:
        return

    x = stack[-1]
    stack.pop()

    sort_stack(stack)

    sorted_insert(stack,x)
    return stack


stack_obj = Stack(5)
stack_obj.push(2)
stack_obj.push(-3)
stack_obj.push(5)
stack_obj.push(9)
stack_obj.push(-7)

print(sort_stack(stack_obj.stack))
