

def noOfLeafNodes(root):
    # Write your code here.
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return noOfLeafNodes(root.left) + noOfLeafNodes(root.right)

