"""
- Topological sort can only be applied to directed acyclic graph
- What is topological sort? Linear ordering of vertices such that for every edge u to v, u always appears before v in that ordering
- logic mean we do dfs and after returning the dfs recursive call put the node for which recursive call(when all neighbours of node are processed) is returned into stack. The stack contains the topological order

Time complexity: O(N+E)
Space complexity: O(N)
"""