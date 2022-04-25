from SingleCircularLinkedList import CircularSingleLinkedList,Node
from LinkedList import LinkedList

def is_circular(head):
    if head is None:
        return True
    elif head.next == head:
        return True
    elif head.next is None:
        return False
    else:
        temp = head.next

        while temp is not None and temp is not head:
            temp = temp.next

        if temp is None:
            return False
        else:
            return True

circular = CircularSingleLinkedList()
circular.create_linked_list(4)
print("above linked list is : ",is_circular(circular.head))

non_circular = LinkedList()
non_circular.generate_list(7,0,100)
print("above linked list is : ",is_circular(non_circular.head))


circular2 = CircularSingleLinkedList()
circular2.create_linked_list(1)
print(is_circular(circular2.head))

non_circular2 = LinkedList()
non_circular2.generate_list(1,0,100)
print(is_circular(non_circular2.head))