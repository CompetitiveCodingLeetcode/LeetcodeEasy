from typing import List

from DFSTraversals import inorder_traversal,preorder_traversal,postorder_traversal
from BFSTraversals import BFSTraversal
from collections import deque
from CountNodes import countNodes, countNodesRecursively
from SumOfNodes import sum_of_nodes
from DiameterOfTree import find_diameter,find_diameter_optimized_approach
from MaximumDepthOfABinaryTree_Q104 import maxDepth
from BinaryTreeInorderTraversal_Q94 import inorderTraversal, inorderTraversal_Morris_traversal
from BinaryTreeNode import BinaryTreeNode
from AverageOfLevelsInBinaryTree_Q637 import Solution
from countLeafNodes import noOfLeafNodes, num_of_leaf_nodes_using_inorder_traversal
from HeightOfTree import height_of_tree
from balancedBinaryTree_Q110 import Solution as balancedBinaryTreeSolution
from IsSumTree import Solution as isSumTreeSolution
from BinaryTreeZigzagLevelOrderTraversal_Q103 import Solution as ZigzagTraversal
from BoundaryOfBinaryTree_Q545 import Solution as BoundaryBT
from VerticalOrderTraversalOfBinaryTree_Q987 import Solution as VerticalOrderTraversal
from TopViewOTree import Solution as TopView
from BottomViewOTree import Solution as BottomView
from LeftViewOfTree import Solution as LeftView
from RightViewOfTree_Q199 import Solution as RightView

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

    def build_from_level_order_traversal(self,root):
        q = deque()
        data = int(input("Enter root data:"))
        root = BinaryTreeNode(data)
        q.append(root)

        while len(q) != 0:
            temp = q.popleft()
            left_data = int(input(f"Enter left data for : {temp.val}"))

            if left_data != -1:
                temp.left = BinaryTreeNode(left_data)
                q.append(temp.left)

            right_data = int(input(f"Enter right data for : {temp.val}"))

            if right_data != -1:
                temp.right = BinaryTreeNode(right_data)
                q.append(temp.right)

        return root



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
    print("height of binary tree:",height_of_tree(root))
    print("number of leaf nodes:",noOfLeafNodes(root))

    # build tree from level order traversal
    root2=BinaryTreeNode()
    btree2 = BinaryTree()
    root2= btree2.build_from_level_order_traversal(root2)
    print(btree2.level_order_traversal_pretty(root2))

    print(countNodes(root))
    print(countNodesRecursively(root))
    print(sum_of_nodes(root))
    print("diameter = ",find_diameter(root))
    print("dimeter by optimized approach=",find_diameter_optimized_approach(root).diameter)
    print("max depth=",maxDepth(root))
    print(inorderTraversal(root))
    print(inorderTraversal_Morris_traversal(root))
    print(Solution().averageOfLevels(root))
    print("Leaf nodes===",noOfLeafNodes(root))
    print(num_of_leaf_nodes_using_inorder_traversal(root))

    print("is balanced flag:",balancedBinaryTreeSolution().isBalanced(root2))
    print("is balanced flag optimized:",balancedBinaryTreeSolution().is_balanced_optimized(root2).is_balanced)

    root3 = BinaryTreeNode()
    btree3 = BinaryTree()
    root3 = btree3.build_from_level_order_traversal(root3)
    print(btree3.level_order_traversal_pretty(root3))
    print("is sum tree:",isSumTreeSolution().is_sum_tree(root3).is_sum_tree)

    print("zig zag level order traversal:",ZigzagTraversal().zigzagLevelOrder(root2))

    print("boundary elements of tree:",BoundaryBT().boundaryOfBinaryTree(root2))

    root4 = BinaryTreeNode()
    btree4 = BinaryTree()
    root4 = btree4.build_from_level_order_traversal(root4)
    print("vertical order traversal: ",VerticalOrderTraversal().verticalTraversal(root4))

    print("top view=",TopView().top_view_of_tree(root2))

    print("bottom view=",BottomView().bottom_view_of_tree(root2))

    # print("left view of tree: ",LeftView().left_view_of_tree(root2))
    print("left view using level order traversal:",LeftView().left_view_of_tree_using_level_order_traversal(root2))

    print("right view using level order traversal:",RightView().rightSideView(root2))


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

