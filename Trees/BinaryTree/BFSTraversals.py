def BFSTraversal(root):
    p_queue = []
    c_queue = []
    p_queue.append(root)
    ans_list=[]
    temp = root
    while temp:
        if temp.right is None and temp.left is None:
            ans_list.append(temp.val)
            # p_queue.pop(0)
            # p_queue[0] = c_queue[0]
            # temp = p_queue[0]
            if c_queue == []:
                temp = None
            else:
                temp = c_queue.pop(0)

            # temp = c_queue[0]
        else:
            if temp.left:
                c_queue.append(temp.left)
            if temp.right:
                c_queue.append(temp.right)
            ans_list.append(temp.val)
            # p_queue.pop(0)
            # p_queue[0] = c_queue[0]
            # temp = p_queue[0]
            if c_queue == []:
                temp = None
            else:
                temp = c_queue.pop(0)
    return ans_list