from typing import List

from DFSTraversals import inorder_traversal,preorder_traversal,postorder_traversal
from BFSTraversals import BFSTraversal
from collections import deque
from CountNodes import countNodes, countNodesRecursively
from SumOfNodes import sum_of_nodes

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
        self.idx += 1

        if node_values[self.idx] == -1:
            return None

        new_node = BinaryTreeNode(node_values[self.idx])
        new_node.left = self.buildTree(node_values)
        new_node.right = self.buildTree(node_values)

        return new_node


    def preorder_traversal(self, root: BinaryTreeNode):

        if root == None:
            return
        print(root.val,end=",")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

    def inorder_traversal(self, root: BinaryTreeNode):
        if root == None:
            return
        inorder_traversal(root.left)
        print(root.val,end=",")
        inorder_traversal(root.right)

    def postorder_traversal(self, root: BinaryTreeNode):
        if root == None:
            return
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val,end=",")

    # here we are storing the entire traversal and printing in one line
    def level_order_traversal(self,root: BinaryTreeNode) -> List[int]:
        if root == None:
            return
        else:
            ans = []
            level_order_traversal_nodes = deque()
            temp = root
            level_order_traversal_nodes.append(temp)
            while len(level_order_traversal_nodes) != 0:
                temp = level_order_traversal_nodes.popleft()
                ans.append(temp.val)
                if temp.left:
                    level_order_traversal_nodes.append(temp.left)
                if temp.right:
                    level_order_traversal_nodes.append(temp.right)
            return ans

    # to store each level traversal in next line for level order traversal
    def level_order_traversal_pretty(self, root: BinaryTreeNode) -> List[int]:
        if root == None:
            return
        else:
            ans = []
            level_nodes = []
            level_order_traversal_nodes = deque()
            temp = root
            level_order_traversal_nodes.append(temp)
            level_order_traversal_nodes.append(None)
            while len(level_order_traversal_nodes) != 0:
                temp = level_order_traversal_nodes.popleft()
                if temp == None:
                    if len(level_order_traversal_nodes) == 0:
                        ans.append(level_nodes)
                        break
                    level_order_traversal_nodes.append(None)
                    ans.append(level_nodes)
                    level_nodes = []
                else:
                    level_nodes.append(temp.val)
                    if temp.left:
                        level_order_traversal_nodes.append(temp.left)
                    if temp.right:
                        level_order_traversal_nodes.append(temp.right)
            return ans




if __name__ == "__main__":
    node_values = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
    btree = BinaryTree()
    root = BinaryTreeNode()
    root = btree.buildTree(node_values)
    print(root.val)
    print("pre order traversal")
    btree.preorder_traversal(root)
    print("inorder traversal")
    btree.inorder_traversal(root)
    print("post order traversal")
    btree.postorder_traversal(root)
    print("level order traversal")
    print(btree.level_order_traversal(root))
    level_order_traversal = btree.level_order_traversal_pretty(root)
    for level_nodes in level_order_traversal:
        for node_val in level_nodes:
            print(node_val,end=" ")
        print()

    print(countNodes(root))
    print(countNodesRecursively(root))
    print(sum_of_nodes(root))


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

