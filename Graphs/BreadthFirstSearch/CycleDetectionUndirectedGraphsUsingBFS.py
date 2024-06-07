"""
Given an undirected graph with V vertices labelled from 0 to V-1 and E edges, check whether it contains any cycle or not. Graph is in the form of adjacency list where adj[i] contains all the nodes ith node is having edge with.

Example 1:

Input:
V = 5, E = 5
adj = {{1}, {0, 2, 4}, {1, 3}, {2, 4}, {1, 3}}
Output: 1
Explanation:

1->2->3->4->1 is a cycle.
Example 2:

Input:
V = 4, E = 2
adj = {{}, {2}, {1, 3}, {2}}
Output: 0
Explanation:

No cycle in the graph.


Your Task:
You don't need to read or print anything. Your task is to complete the function isCycle() which takes V denoting the number of vertices and adjacency list as input parameters and returns a boolean value denoting if the undirected graph contains any cycle or not, return 1 if a cycle is present else return 0.

NOTE: The adjacency list denotes the edges of the graph where edges[i] stores all other vertices to which ith vertex is connected.



Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)




Constraints:
1 ≤ V, E ≤ 105




main logic: If visited is true and node != parent in case of bfs traversal then cycle is present.
maintain one more data str for parent of every node

can be done using BFS as well as DFS.
"""

from typing import List
import queue as q


class Solution:
    def detect_cycle_bfs(self, i, visited, adj_list, num_of_nodes):
        parent = {}
        bfs_q = q.Queue(maxsize=num_of_nodes)
        visited[i] = True
        parent[i] = -1
        bfs_q.put(i)

        while not bfs_q.empty():
            element = bfs_q.get()
            neighbors = adj_list[element]
            for neighbor in neighbors:
                if (neighbor in visited.keys()) and (parent[element] != neighbor):
                    return True
                elif neighbor not in visited.keys():
                    bfs_q.put(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = element
        return False

        # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:

        adj_list = {}
        for i in range(0, len(adj)):
            adj_list[i] = adj[i]

            # Code here
        visited = {}
        for i in range(0, V):
            if i not in visited.keys():
                ans = self.detect_cycle_bfs(i, visited, adj_list, V)
            if ans:
                return ans
        return False

sol = Solution()
# here first parameter is number of nodes or vertices in graph,
# second parameter gives ith node is connected to which other nodes.
print(sol.isCycle(4,[[],[2],[1,3],[2]]))