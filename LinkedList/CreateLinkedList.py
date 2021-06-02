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

    def insert(self,n):
        temp = self.head

        for i in range(n):
            node = Node(i)
            if single_linked_list_obj.head == None:
                temp = node
                single_linked_list_obj.head = temp
            else:
                temp.next = node
                temp = node

    def traverse(self):
        temp1 = self.head
        while temp1:
            print("Inside")
            print(temp1.val)
            temp1 = temp1.next


single_linked_list_obj = SingleLinkedList()
single_linked_list_obj.insert(5)
single_linked_list_obj.traverse()
