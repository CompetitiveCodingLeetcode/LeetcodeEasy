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


class BinaryTree:
    def __init__(self):
        self.root = None
        self.idx = -1

    def buildTree(self,node_values = []) -> BinaryTreeNode:

        print("node values=",node_values)

        self.idx += 1

        if node_values[self.idx] == -1:
            return None

        new_node = BinaryTreeNode(node_values[self.idx])
        new_node.left = self.buildTree(node_values)
        new_node.right = self.buildTree(node_values)

        return new_node

if __name__ == "__main__":
    node_values = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
    btree = BinaryTree()
    root = BinaryTreeNode()
    root = btree.buildTree(node_values)
    print(root.val)

# newBT = BinaryTreeNode("Drinks")
# leftChild = BinaryTreeNode("Hot")
# rightChild = BinaryTreeNode("Cold")
# newBT.left = leftChild
# newBT.right = rightChild
# coffee = BinaryTreeNode("Coffee")
# tea = BinaryTreeNode("Tea")
# pepsi = BinaryTreeNode("Pepsi")
# cola = BinaryTreeNode("Cola")
# leftChild.left = coffee
# leftChild.right = tea
# rightChild.left = pepsi
# rightChild.right = cola
#
# preorder_traversal(newBT)
# print()
# postorder_traversal(newBT)
# print()
# inorder_traversal(newBT)
# print()
# print(BFSTraversal(newBT))

