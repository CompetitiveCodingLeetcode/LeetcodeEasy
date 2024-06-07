"""
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