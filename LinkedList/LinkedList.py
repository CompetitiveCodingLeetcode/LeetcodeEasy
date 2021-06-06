from random import randint


class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self, values=None):
        self.head = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

    def __str__(self):
        values = [str(x.val) for x in self]
        return '->'.join(values)

    def __len__(self):
        temp = self.head
        list_length = 0
        while temp:
            list_length += 1
            temp = temp.next
        return list_length

    def add(self, node):
        temp = self.head
        if temp is None:
            temp = node
            self.head = temp
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        return self

    def generate_list(self, n, min_val, max_val):
        for i in range(n):
            node = Node(randint(min_val, max_val))
            self.add(node)
        return self


customLL = LinkedList()
customLL.generate_list(10, 0, 99)
print(customLL)
print(len(customLL))