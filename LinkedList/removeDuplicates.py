from LinkedList import LinkedList


# remove duplicates in unsorted linked list
# this approach uses a temporary buffer hence Space complexity = O(n) and time complexity is O(n)
# if temporary buffer is not to be used then Time complexity will be O(n^2)

def remove_dups(linked_list):
    temp = linked_list.head
    if temp is None:
        return
    else:
        visited_nodes = {temp.val: 1}
        while temp.next:
            if temp.next.val in visited_nodes:
                temp.next = temp.next.next
            else:
                visited_nodes[temp.next.val] = 1
                temp = temp.next
        return linked_list


linked_list = LinkedList()
linked_list.generate_list(10, 0, 99)
print(linked_list)
remove_dups(linked_list)
print(linked_list)

# TODO: remove duplicates from sorted linked list
# TODO: sort linked list using merge sort
