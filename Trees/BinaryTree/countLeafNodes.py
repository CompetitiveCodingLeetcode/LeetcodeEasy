

def noOfLeafNodes(root):
    # Write your code here.
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return noOfLeafNodes(root.left) + noOfLeafNodes(root.right)

def inorder_traversal(root,count):
    if root is None:
        return

    inorder_traversal(root.left,count)
    if root.left is None and root.right is None:
        print("count===",count)
        count += 1
    inorder_traversal(root.right,count)

def num_of_leaf_nodes_using_inorder_traversal(root):
    count = 0
    inorder_traversal(root,count)
    return count





