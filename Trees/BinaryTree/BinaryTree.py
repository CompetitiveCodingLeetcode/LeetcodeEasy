from DFSTraversals import inorder_traversal,preorder_traversal,postorder_traversal
from BFSTraversals import BFSTraversal


class BinaryTreeNode:
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None
    #
    # def __str__(self):
    #     return str(self.val)


# class BinaryTree:
#     def __init__(self, values=None):
#         self.root = None

newBT = BinaryTreeNode("Drinks")
leftChild = BinaryTreeNode("Hot")
rightChild = BinaryTreeNode("Cold")
newBT.left = leftChild
newBT.right = rightChild
coffee = BinaryTreeNode("Coffee")
tea = BinaryTreeNode("Tea")
pepsi = BinaryTreeNode("Pepsi")
cola = BinaryTreeNode("Cola")
leftChild.left = coffee
leftChild.right = tea
rightChild.left = pepsi
rightChild.right = cola

preorder_traversal(newBT)
print()
postorder_traversal(newBT)
print()
inorder_traversal(newBT)
print(BFSTraversal(newBT))

