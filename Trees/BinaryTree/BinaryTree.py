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
from DiagonalTraversalOfBinaryTree import Solution as DiagonalTraversal
from sumOfNodesInLongestPathFromRootToLeaf import Solution as SumLongestPathRootToLeaf
from LowestCommonAncestor_Q236 import Solution as LCA
from PathSum_Q112 import Solution as PathSum1
from PathSum2_Q113 import Solution as PathSum2
from PathSum3_Q437 import Solution as PathSum3


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

    def find_position(self,inorder_traversal,element,n):
        for i in range(0,n):
            if inorder_traversal[i] == element:
                return i

        return -1


    def solve(self,preorder_traersal,inorder_traversal,preorder_idx,inorder_start_idx,inorder_end_idx,n):

        #base case
        if preorder_idx >= n or (inorder_start_idx > inorder_end_idx):
            return None

        element = preorder_traersal[preorder_idx]
        preorder_idx += 1
        root = BinaryTreeNode(element)
        pos = self.find_position(inorder_traversal,element,n)

        # recursive calls
        root.left = self.solve(preorder_traersal,inorder_traversal,preorder_idx,inorder_start_idx,pos-1,n)
        root.right = self.solve(preorder_traersal,inorder_traversal,preorder_idx,pos+1,inorder_end_idx,n)

        return root


    def build_tree_from_preorder_inorder_traversal(self,preorder_traversal, inorder_traversal, n):
        """
        q 105
        Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.



        Example 1:


        Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        Output: [3,9,20,null,null,15,7]
        Example 2:

        Input: preorder = [-1], inorder = [-1]
        Output: [-1]


        Constraints:

        1 <= preorder.length <= 3000
        inorder.length == preorder.length
        -3000 <= preorder[i], inorder[i] <= 3000
        preorder and inorder consist of unique values.
        Each value of inorder also appears in preorder.
        preorder is guaranteed to be the preorder traversal of the tree.
        inorder is guaranteed to be the inorder traversal of the tree.
        """
        pre_order_idx = 0
        ans = self.solve(preorder_traversal,inorder_traversal,pre_order_idx,0,n-1,n)
        print("postorder traversal of tree built from inorder and preorder traversal is:",self.postorder_traversal(ans))



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
    print("sum of nodes:")
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
    print("right view of tree using recursion:",RightView().right_view_using_recursion(root2))
    print("diagonal traversal:",DiagonalTraversal().diagonal_traversal(root2))

    print("sum of node in longest path from root to leaf node:",SumLongestPathRootToLeaf().sum_of_long_root_to_leaf_node(root2))

    # root = [3,5,1,6,2,0,8,-1,-1,7,4], p = 5, q = 4
    print("For LCA")
    root5 = BinaryTreeNode()
    btree5 = BinaryTree()
    root5 = btree5.build_from_level_order_traversal(root5)
    print("LCA by recursion:",LCA().lowestCommonAncestor(root5,5,4).val)

    #root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    print("For Path Sum 1:")
    root6 = BinaryTreeNode()
    btree6 = BinaryTree()
    root6 = btree6.build_from_level_order_traversal(root6)
    print("Path sum 1 = ",PathSum1().hasPathSum(root6,22))

    # root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    # o/p: [[5,4,11,2],[5,8,4,5]]
    print("For Path Sum2:")
    root7 = BinaryTreeNode()
    btree7 = BinaryTree()
    root7 = btree7.build_from_level_order_traversal(root7)
    print("Path sum2 =",PathSum2().pathSum(root7,22))

    #Input: root = [10, 5, -3, 3, 2, null, 11, 3, -2, null, 1], targetSum = 8
    #Output: 3
    print("For Path Sum3:")
    root8 = BinaryTreeNode()
    btree8 = BinaryTree()
    root8 = btree8.build_from_level_order_traversal(root8)
    print("Path sum3 =", PathSum3().pathSum(root8, 8))

    # q105 construct binary tree from preorder and inorder traversal
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    btree.build_tree_from_preorder_inorder_traversal(preorder,inorder,5)

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

