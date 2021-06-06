class Node:
    def __init__(self, value=None):
        self.val = value
        self.prev = None
        self.next = None


class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next
            if temp == self.head:
                break

    def create_List(self, num_of_nodes):
        temp = self.head
        for i in range(num_of_nodes):
            node = Node(i + 1)
            if i == 0:
                temp = node
                self.head = node
                self.head.next = self.head
                self.head.prev = self.head
            else:
                temp.next = node
                node.prev = temp
                temp = temp.next
                node.next = self.head
                self.head.prev = node

    def insert_in_beginning(self, node):
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node
        self.head = node

    def insert_in_end(self, node):
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node

    def insert_after_node(self, node, loc):
        temp = self.head
        for i in range(loc):
            temp = temp.next
        node.next = temp.next
        node.prev = temp
        temp.next.prev = node
        temp.next = node

    def search_node(self, node_value):
        temp = self.head
        idx = -1
        if temp.val == node_value:
            idx += 1
            return idx
        else:
            temp = temp.next
            idx += 1
            while temp is not self.head:
                idx += 1
                if temp.val == node_value:
                    return idx
                else:
                    temp = temp.next
        return -1

    def delete_node_from_beginning(self):
        temp = self.head
        self.head = temp.next
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

    def delete_from_end(self):
        temp = self.head.prev
        self.head.prev = temp.prev
        temp.prev.next = self.head
        temp.prev = None

    def delete_after_node(self, loc):
        temp = self.head
        for i in range(loc):
            temp = temp.next
        temp.next.next.prev = temp
        temp.next.prev = None
        temp.next = temp.next.next

    def delete_linked_list(self):
        temp = self.head
        if temp is not None:
            temp.prev = None
            temp = temp.next
        while temp is not self.head:
            temp.prev = None
            temp = temp.next
        self.head = None

    def traverse_linked_list(self):
        temp = self.head
        if temp is not None:
            print(temp.val)
            temp = temp.next
        while temp is not self.head:
            print(temp.val)
            temp = temp.next


circular_double_linked_list_obj = CircularDoubleLinkedList()

circular_double_linked_list_obj.create_List(3)
print([node.val for node in circular_double_linked_list_obj])

node = Node(11)
circular_double_linked_list_obj.insert_in_beginning(node)
print([node.val for node in circular_double_linked_list_obj])

node = Node(12)
circular_double_linked_list_obj.insert_in_end(node)
print([node.val for node in circular_double_linked_list_obj])

node = Node(13)
loc = circular_double_linked_list_obj.search_node(2)
print("loc=", loc)
circular_double_linked_list_obj.insert_after_node(node, loc)
print([node.val for node in circular_double_linked_list_obj])

circular_double_linked_list_obj.delete_node_from_beginning()
print([node.val for node in circular_double_linked_list_obj])

circular_double_linked_list_obj.delete_from_end()
print([node.val for node in circular_double_linked_list_obj])

loc = circular_double_linked_list_obj.search_node(2)
print("loc=", loc)
circular_double_linked_list_obj.delete_after_node(loc)
print([node.val for node in circular_double_linked_list_obj])

circular_double_linked_list_obj.traverse_linked_list()

circular_double_linked_list_obj.delete_linked_list()
print([node.val for node in circular_double_linked_list_obj])
