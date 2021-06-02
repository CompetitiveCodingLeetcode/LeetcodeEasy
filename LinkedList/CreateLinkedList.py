"""
Create a linked list with values corresponding to natural numbers
"""


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None


single_linked_list_obj = SingleLinkedList()
temp = single_linked_list_obj.head


for i in range(4):
    node = Node(i)
    if single_linked_list_obj.head == None:
        print("Inserting first node")
        temp = node
        single_linked_list_obj.head = temp
    else:
        temp.next = node
        temp = node


temp1 = single_linked_list_obj.head
print("temp1=",temp1)
for i in range(4):
        print("Inside")
        print(temp1.val)
        temp1= temp1.next
