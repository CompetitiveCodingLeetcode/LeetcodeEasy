"""
Algo to do topological sort using BFS or Kahn's Algorithm:
1. Find indegree of all nodes
2. create a queue and insert all nodes with indegree 0
3. do BFS
when you pop a node from queue, all the neighbor nodes indegree is decreased by 1
and all those nodes whose indegree now becomes 0 are pushed in queue.
store popped element in ans

Time complexity: O(N+E)
space complexity: O(N+E)
"""
import queue as q

class Solution:

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):

        adj_list = {}
        for i in range(0, len(adj)):
            adj_list[i] = adj[i]

        indegree = [0] * V

        for k, v in adj_list.items():
            if len(v) > 0:
                for i in v:
                    indegree[i] += 1

        ans = []
        kahns_bfs_q = q.Queue(maxsize=V)

        for i in range(0, V):
            if indegree[i] == 0:
                kahns_bfs_q.put(i)

        while (not kahns_bfs_q.empty()):
            element = kahns_bfs_q.get()
            ans.append(element)

            for neighbor in adj_list[element]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    kahns_bfs_q.put(neighbor)

        return ans

sol1 = Solution()
print(sol1.topoSort(4,[[1,2,3],[],[],[]]))

sol2 = Solution()
print(sol2.topoSort(6,[[4,5],[4],[5],[1,2],[],[]]))