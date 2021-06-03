"""
Create a linked list with values corresponding to natural numbers
"""


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next


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

    def insert_after_given_node(self, node, loc):
        temp_ptr = self.head
        for i in range(loc):
            temp_ptr = temp_ptr.next
        node.next = temp_ptr.next
        temp_ptr.next = node

    def search_node(self,value):
        temp = self.head
        loc = 0
        while temp.val != value:
            temp = temp.next
            loc+=1
        return loc


single_linked_list_obj = SingleLinkedList()

single_linked_list_obj.create(5)
print([node.val for node in single_linked_list_obj])

node = Node(3)
single_linked_list_obj.insert_in_beginning(node)
print("traversal after insertion in beginning")
print([node.val for node in single_linked_list_obj])

node = Node(3)
single_linked_list_obj.insert_in_end(node)
print("traversal after insertion in end")
print([node.val for node in single_linked_list_obj])

node = Node(45)
loc = single_linked_list_obj.search_node(3)
print("loc=",loc)
single_linked_list_obj.insert_after_given_node(node,loc)
print("Insertion after a given node")
print([node.val for node in single_linked_list_obj])
