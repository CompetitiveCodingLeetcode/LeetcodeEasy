"""
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.


Example 1:

Input:



Output: 1
Explanation: 3 -> 3 is a cycle

Example 2:

Input:


Output: 0
Explanation: no cycle in the graph

Your task:
You dont need to read input or print anything. Your task is to complete the function isCyclic() which takes the integer V denoting the number of vertices and adjacency list adj as input parameters and returns a boolean value denoting if the given directed graph contains a cycle or not.
In the adjacency list adj, element adj[i][j] represents an edge from i to j.


Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)


Constraints:
1 ≤ V, E ≤ 105

Approach: Undirected graph logic does not work for directed graphs,try doing dry run with[[1,2][1,3][2,3].
Hence, we need to make extra data str to get for what nodes dis call has gone hence the nodes dis call is set to true, before making call and set to false after returning.
If for any node the dfs call has gone and the node is also visited then cycle exists.
"""

from typing import List


class Solution:
    def isCycleDFS(self, i, adj_list, visited, dfs_visited):
        visited[i] = True
        dfs_visited[i] = True

        for neighbor in adj_list[i]:
            if (neighbor not in visited.keys()):
                ans = self.isCycleDFS(neighbor, adj_list, visited, dfs_visited)
                if ans:
                    return True
            elif neighbor in dfs_visited.keys() and dfs_visited[neighbor]:
                return True

        dfs_visited[i] = False
        return False

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        # code here
        adj_list = {}
        for i in range(0, len(adj)):
            adj_list[i] = adj[i]
        visited = {}
        dfs_visited = {}
        for i in range(0, V):
            if i not in visited.keys():
                ans = self.isCycleDFS(i, adj_list, visited, dfs_visited)

            if ans:
                return True
        return False

sol = Solution()
print(sol.isCyclic(4,[[],[0],[1],[2,3]]))

sol2 = Solution()
print(sol2.isCyclic(3,[[],[0],[1]]))
