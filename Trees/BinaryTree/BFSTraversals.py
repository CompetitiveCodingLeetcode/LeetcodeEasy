def BFSTraversal(root):
    c_queue = []
    ans_list=[]
    temp = root
    while temp:
        if temp.right is not None or temp.left is not None:
            if temp.left:
                c_queue.append(temp.left)
            if temp.right:
                c_queue.append(temp.right)
        ans_list.append(temp.val)
        if c_queue == []:
            temp = None
        else:
            temp = c_queue.pop(0)
    return ans_list