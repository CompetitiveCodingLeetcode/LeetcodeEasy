class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class CircularSingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next
            if temp == self.tail.next:
                break

    def create_linked_list(self, num_of_nodes):
        for i in range(num_of_nodes):
            node = Node(i + 1)
            if self.head is None:
                self.head = node
            else:
                self.tail.next = node
            self.tail = node
            node.next = self.head

    def delete_linked_list(self):
        self.head = None
        self.tail = None

    def search_node(self, value):
        temp = self.head
        idx = -1
        while temp:
            idx += 1
            if temp.val == value:
                return idx
            temp = temp.next
            if temp == self.tail.next:
                break
        if idx == -1:
            return idx

    def insert_in_beginning(self, node):
        node.next = self.head
        self.tail.next = node
        self.head = node

    def insert_in_end(self, node):
        self.tail.next = node
        node.next = self.head
        self.tail = node

    def insert_after_given_node(self, loc, node):
        temp = self.head
        for i in range(loc):
            temp = temp.next
        node.next = temp.next
        temp.next = node

    def delete_node_from_beginning(self):
        temp = self.head
        self.head = temp.next
        self.tail.next = self.head
        print("deleted node value = ", temp.val)

    def delete_node_from_end(self):
        temp = self.head
        while temp:
            if temp.next == self.tail:
                break
            temp = temp.next
        print("deleted node value=", self.tail.val)
        temp.next = self.head
        self.tail = temp

    def delete_node_after_node(self, loc):
        temp = self.head
        for i in range(loc - 1):
            temp = temp.next
        node = temp.next
        print("node to be deleted=", node.val)
        temp.next = node.next

    def traverse_linked_list(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
            if temp == self.tail.next:
                break


single_circular_linked_list = CircularSingleLinkedList()

print([node.val for node in single_circular_linked_list])
single_circular_linked_list.create_linked_list(5)
print([node.val for node in single_circular_linked_list])

node = Node(12)
single_circular_linked_list.insert_in_beginning(node)
print([node.val for node in single_circular_linked_list])

node = Node(13)
single_circular_linked_list.insert_in_end(node)
print([node.val for node in single_circular_linked_list])

loc = single_circular_linked_list.search_node(3)
print("loc=", loc)
node = Node(14)
try:
    single_circular_linked_list.insert_after_given_node(loc, node)
except TypeError:
    print("Value not found in linked list")
print([node.val for node in single_circular_linked_list])

single_circular_linked_list.delete_node_from_beginning()
print([node.val for node in single_circular_linked_list])

single_circular_linked_list.delete_node_from_end()
print([node.val for node in single_circular_linked_list])

loc = single_circular_linked_list.search_node(14)
print("loc=", loc)
try:
    single_circular_linked_list.delete_node_after_node(loc)
except TypeError:
    print("Value to be deleted not found in the list")
print([node.val for node in single_circular_linked_list])

single_circular_linked_list.traverse_linked_list()

single_circular_linked_list.delete_linked_list()
print([node.val for node in single_circular_linked_list])
