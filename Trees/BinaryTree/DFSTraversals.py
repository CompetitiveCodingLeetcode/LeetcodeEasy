def inorder_traversal(root):
    if root is None:
        return
    else:
        inorder_traversal(root.left)
        print(root.data,end=",")
        inorder_traversal(root.right)


def preorder_traversal(root):
    if root is None:
        return
    else:
        print(root.data,end=",")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    if root is None:
        return
    else:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data,end=",")

