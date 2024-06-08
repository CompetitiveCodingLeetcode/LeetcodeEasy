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
