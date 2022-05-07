"""
delete the middle element of stack
"""


def find_mid_and_delete(stack, size, count):
    # base case
    if count == size//2:
        stack.pop()
        return

    num = stack[-1]
    stack.pop()

    #recursive call
    find_mid_and_delete(stack,size,count+1)

    stack.append(num)

    return stack


def delete_mid_element_in_stack(stack,size):
    count = 0
    stack = find_mid_and_delete(stack,size,count)
    print(stack)


delete_mid_element_in_stack([1,2,3,4,5],5)