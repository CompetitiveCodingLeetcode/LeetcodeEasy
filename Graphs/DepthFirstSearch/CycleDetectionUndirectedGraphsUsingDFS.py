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




main logic: If visited is true and node != parent in case of dfs traversal then cycle is present.
in dfs recursive call you send current node as parent. so one more parameter for parent in recursive method call.

cycle detection can be done using BFS as well as DFS.
"""

from typing import List


class Solution:
    def detectCycleDFS(self, node, parent, visited, adj_list):
        visited[node] = True
        for neighbor in adj_list[node]:
            if neighbor not in visited.keys():
                ans = self.detectCycleDFS(neighbor, node, visited, adj_list)
                if ans:
                    return True
            elif neighbor != parent:
                return True
        return False

        # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Code here
        adj_list = {}

        for i in range(0, len(adj)):
            adj_list[i] = adj[i]
        visited = {}
        for i in range(0, V):
            if i not in visited.keys():
                ans = self.detectCycleDFS(i, -1, visited, adj_list)
            if ans:
                return True
        return False

sol = Solution()
# here first parameter is number of nodes or vertices in graph,
# second parameter gives ith node is connected to which other nodes.
print(sol.isCycle(4,[[],[2],[1,3],[2]]))