from collections import deque
from SearchBST_Q700 import searchBST,searchBST_iterative
from BSTNode import BSTNode


class BST:
    def insert(self, root, key):
        if root is None:
            return BSTNode(key)

        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def inorder_traversal(self, root):
        if root is None:
            return None
        else:
            self.inorder_traversal(root.left)
            print(root.val, end=",")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root is None:
            return None
        else:
            print(root.val, end=",")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root is None:
            return None
        else:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.val,end=",")

    def level_order_traversal(self,root):
        level_order_nodes = deque()
        if root is None:
            return None
        temp = root
        level_order_nodes.append(temp)
        while len(level_order_nodes) != 0:
            temp = level_order_nodes.popleft()
            print(temp.val,end=",")
            if temp.left:
                level_order_nodes.append(temp.left)
            if temp.right:
                level_order_nodes.append(temp.right)

    def find_max_in_BST(self,root) -> int:
        temp = root
        if temp is None:
            return
        while temp.right is not None:
            temp = temp.right
        return temp.val

    def find_min_in_BST(self,root) -> int:
        temp = root
        if temp is None:
            return
        while temp.left is not None:
            temp = temp.left
        return temp.val

binary_search_tree = BST()
root = BSTNode(5)
# Insertion time complexity: O(log n)
binary_search_tree.insert(root, 5)
binary_search_tree.insert(root, 7)
binary_search_tree.insert(root, 9)
binary_search_tree.insert(root, 10)
binary_search_tree.insert(root, 3)
binary_search_tree.insert(root, 1)
binary_search_tree.insert(root, 2)
binary_search_tree.insert(root, 4)
print("Preorder traversal")
binary_search_tree.preorder_traversal(root)
print()
print("Inorder traversal")
# observation: Inorder traversal of BST is sorted
binary_search_tree.inorder_traversal(root)
print()
print("Postorder traversal")
binary_search_tree.postorder_traversal(root)
print()
print("Level order traversal")
binary_search_tree.level_order_traversal(root)
print()
temp = searchBST(root,3)
print("subtree after searching:")
binary_search_tree.preorder_traversal(temp)
temp = searchBST_iterative(root,3)
print("subtree after searching:")
binary_search_tree.preorder_traversal(temp)
# time complexity: O(height)
print("\nmax in BST:",binary_search_tree.find_max_in_BST(root))
# time complexity: O(height)
print("min in BST:",binary_search_tree.find_min_in_BST(root))