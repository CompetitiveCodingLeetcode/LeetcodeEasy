from collections import deque

# count nodes using BFS complexity: O(n)
def countNodes(root):
    if root == None:
        return 0
    else:
        tree_nodes_queue = deque()
        nodes_count = 0
        temp = root
        tree_nodes_queue.append(temp)
        while len(tree_nodes_queue) != 0:
            temp = tree_nodes_queue.popleft()
            if temp.left:
                tree_nodes_queue.append(temp.left)
            if temp.right:
                tree_nodes_queue.append(temp.right)
            nodes_count += 1

        return nodes_count


def countNodesRecursively(root):
    if root == None:
        return 0

    nodes_in_left_subtree = countNodesRecursively(root.left)
    nodes_in_right_subtree = countNodesRecursively(root.right)

    return nodes_in_right_subtree + nodes_in_left_subtree + 1
