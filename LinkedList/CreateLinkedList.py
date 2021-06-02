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

    def create(self,n):
        temp = self.head

        for i in range(n):
            node = Node(i)
            if single_linked_list_obj.head is None:
                temp = node
                single_linked_list_obj.head = temp
            else:
                temp.next = node
                temp = node

    def traverse(self):
        temp1 = self.head
        while temp1:
            print(temp1.val)
            temp1 = temp1.next

    def insert_in_beginning(self,node):
        node.next = self.head
        self.head = node



single_linked_list_obj = SingleLinkedList()
single_linked_list_obj.create(5)
single_linked_list_obj.traverse()
node = Node(3)
single_linked_list_obj.insert_in_beginning(node)
print("traversal after insertion in beginning")
single_linked_list_obj.traverse()
