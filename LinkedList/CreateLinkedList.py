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

    def insert_in_end(self, node):
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def insert_after_given_node(self, node, after_node):
        temp = self.head
        while temp.val != after_node.val:
            temp = temp.next
        node.next = temp.next
        temp.next = node

    # def search_node(self,value):
    #     temp = self.head
    #     while temp.val !=

single_linked_list_obj = SingleLinkedList()

single_linked_list_obj.create(5)
single_linked_list_obj.traverse()

node = Node(3)
single_linked_list_obj.insert_in_beginning(node)
print("traversal after insertion in beginning")
single_linked_list_obj.traverse()

node = Node(3)
single_linked_list_obj.insert_in_end(node)
print("traversal after insertion in end")
single_linked_list_obj.traverse()



