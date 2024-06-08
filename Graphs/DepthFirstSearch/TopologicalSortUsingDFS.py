"""
Given an adjacency list for a Directed Acyclic Graph (DAG) where adj_list[i] contains a list of all vertices j such that there is a directed edge from vertex i to vertex j, with  V  vertices and E  edges, your task is to find any valid topological sorting of the graph.



In a topological sort, for every directed edge u -> v,  u must come before v in the ordering.



Example 1:

Input:

Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible Topological order for the
graph is 3, 2, 1, 0.
Example 2:

Input:

Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible Topological order for the
graph is 3, 2, 1, 0, 5, 4.
Your Task:
You don't need to read input or print anything. Your task is to complete the function topoSort()  which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns an array consisting of the vertices in Topological order. As there are multiple Topological orders possible, you may return any of them. If your returned topo sort is correct then the console output will be 1 else 0.

Expected Time Complexity: O(V + E).
Expected Auxiliary Space: O(V).

Constraints:
2 ≤ V ≤ 104
1 ≤ E ≤ (N*(N-1))/2

- Topological sort can only be applied to directed acyclic graph
- What is topological sort? Linear ordering of vertices such that for every edge u to v, u always appears before v in that ordering
- logic mean we do dfs and after returning the dfs recursive call put the node for which recursive call(when all neighbours of node are processed) is returned into stack. The stack contains the topological order

Time complexity: O(N+E)
Space complexity: O(N)
"""


class Solution:

    def find_topological_order(self, i, adj_list, visited, topological_order_stack):
        visited[i] = True

        for neighbor in adj_list[i]:
            if neighbor not in visited.keys():
                self.find_topological_order(neighbor, adj_list, visited, topological_order_stack)

        topological_order_stack.append(i)

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):

        adj_list = {}
        for i in range(0, len(adj)):
            adj_list[i] = adj[i]

        # Code here
        visited = {}
        topological_order_stack = []
        ans = []
        for i in range(0, V):
            if i not in visited.keys():
                self.find_topological_order(i, adj_list, visited, topological_order_stack)

        i = len(topological_order_stack)
        while i > 0:
            ans.append(topological_order_stack[i - 1])
            i -= 1

        return ans

sol1 = Solution()
print(sol1.topoSort(4,[[1,2,3],[],[],[]]))

sol2 = Solution()
print(sol2.topoSort(6,[[4,5],[4],[5],[1,2],[],[]]))
