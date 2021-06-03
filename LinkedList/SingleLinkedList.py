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

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next


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
        if self.head is None:
            print("The list does not exist")
        else:
            temp = self.head
            loc = 0
            while temp:
                if temp.val == value:
                    return loc
                loc+=1
                temp = temp.next
            return "The element does not exist"

    def delete_node_from_beginning(self):
        if self.head is None:
            return "Empty linked list"
        else:
            temp = self.head
            self.head = self.head.next
            return temp.val

    def delete_node_from_end(self):
        if self.head is None:
            return "Empty linked list"
        else:
            temp = self.head
            while temp.next is not None:
                prev = temp
                temp = temp.next
            prev.next = None
            return temp.val

    def delete_node_after_given_node(self,loc):
        temp = self.head
        for i in range(loc):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        return temp.val

    def delete_linked_list(self):
        if self.head:
            self.head = None
        else:
            print("linked list does not exist")


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

value = single_linked_list_obj.delete_node_from_beginning()
print("value deleted = ",value)
print("traversal after deletion from beginning")
print([node.val for node in single_linked_list_obj])

value = single_linked_list_obj.delete_node_from_end()
print("value deleted = ",value)
print("traversal after deletion from end")
print([node.val for node in single_linked_list_obj])

loc = single_linked_list_obj.search_node(2)
print("loc=",loc)
value = single_linked_list_obj.delete_node_after_given_node(loc)
print("value deleted = ",value)
print("traversal after deletion")
print([node.val for node in single_linked_list_obj])

print("linked list before deletion")
print([node.val for node in single_linked_list_obj])
single_linked_list_obj.delete_linked_list()
print("linked list after deletion")
print([node.val for node in single_linked_list_obj])
