"""

APPROACH:
Use bfs to fill parent array while doing bfs.
You have src and dest given, backtrack in parents array from dest to source
and append in ans using parent of curr node and
ans is reverse of you have stored as you traversed from dest to src.


complete sol for https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
"""

import queue as q


class Solution:
    def find_shortest_path_bfs(self, i, adj_list, visited, bfs_queue, parent):
        visited[i] = True
        parent[i] = -1
        bfs_queue.put(i)

        while not bfs_queue.empty():
            element = bfs_queue.get()
            for neighbor in adj_list[element]:
                if neighbor not in visited.keys():
                    parent[neighbor] = element
                    visited[neighbor] = True
                    bfs_queue.put(neighbor)

    def shortestPath(self, edges, n, m, src,dest):
        # code here
        adj_list = {}
        for i in range(0, len(edges)):
            adj_list[i] = edges[i]

        print("adj list====",adj_list)
        visited = {}
        bfs_queue = q.Queue(maxsize=n)
        parent = {}

        self.find_shortest_path_bfs(src, adj_list, visited, bfs_queue, parent)

        temp = dest
        path = []
        path.append(temp)
        while temp != src:
            temp = parent[temp]
            path.append(temp)
        print("path===",path)
        path.reverse()
        return path

sol1 = Solution()
print(sol1.shortestPath([[1,3],[0,2],[1,6],[0,4],[3,5],[4,6],[2,5,7,8],[6,8],[6,7]],9,10,0,6))

# print(sol1.shortestPath([[0,0],[1,1],[1,3],[3,0]],4,4,0,1))