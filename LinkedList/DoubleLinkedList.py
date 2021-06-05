class Node:
    def __init__(self, value=None):
        self.val = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

    def create_List(self, num_of_nodes):
        temp = self.head
        for i in range(num_of_nodes):
            node = Node(i + 1)
            if i == 0:
                self.head = node
                node.prev = None
                node.next = None
                temp = node
            else:
                print("i=",i)
                node.prev = temp
                node.next = None
                temp.next = node
                temp = node

    def insert_in_beginning(self,node):
        temp = self.head
        node.next = temp
        temp.prev = node
        self.head = node

    def insert_in_end(self,node):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node
        node.prev = temp

    def insert_after_node(self,node,loc):
        temp = self.head
        for i in range(loc):
            temp = temp.next
        node.next = temp.next
        temp.next = node
        node.prev = temp
        temp = node.next
        temp.prev = node

    def search_node(self,value):
        temp = self.head
        idx =-1
        while temp:
            idx+=1
            if temp.val == value:
                return idx
            temp = temp.next
        return idx

    def delete_node_from_beginning(self):
        temp = self.head
        print("value deleted = ",temp.val)
        self.head = temp.next
        self.head.prev = None

    def delete_from_end(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        print("value deleted = ",temp.val)
        temp.prev.next = None
        temp.prev = None

    def delete_after_node(self,loc):
        temp = self.head
        for i in range(loc):
            temp = temp.next
        prev_node = temp.prev
        prev_node.next = temp.next
        temp.next.prev = prev_node

    def delete_linked_list(self):
        self.head = None

    def traverse_linked_list(self):
        temp = self.head
        while temp:
            print(temp.val,end=" ")
            temp = temp.next


double_linked_list_obj = DoubleLinkedList()
double_linked_list_obj.create_List(3)
print([node.val for node in double_linked_list_obj])

node = Node(11)
double_linked_list_obj.insert_in_beginning(node)
print([node.val for node in double_linked_list_obj])

node = Node(12)
double_linked_list_obj.insert_in_end(node)
print([node.val for node in double_linked_list_obj])

node = Node(13)
loc = double_linked_list_obj.search_node(3)
print("loc=",loc)
double_linked_list_obj.insert_after_node(node,loc)
print([node.val for node in double_linked_list_obj])

double_linked_list_obj.delete_node_from_beginning()
print([node.val for node in double_linked_list_obj])

double_linked_list_obj.delete_from_end()
print([node.val for node in double_linked_list_obj])

loc = double_linked_list_obj.search_node(3)
print("loc=",loc)
double_linked_list_obj.delete_after_node(loc)
print([node.val for node in double_linked_list_obj])

double_linked_list_obj.traverse_linked_list()

double_linked_list_obj.delete_linked_list()
print("\n",[node.val for node in double_linked_list_obj])
