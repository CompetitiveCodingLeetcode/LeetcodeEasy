## Graphs
- contains nodes and edges
- Node: an entity which can store any type of data
- edges: for connection of nodes
- for undirected graphs:
  - Degree of node: number of edges connected to the node
- For directed graphs:
  - Indegree of node: no of edges coming towards the node
  - Outdegree of node: no of edges going away from node
- weighted graphs: graphs with weights on edges between two nodes. If no weights are given and we need to apply algos related to weights then assume weights to be 1.
  - directed weighted graphs: directed graphs with weights on edges
  - undirected weighted graphs: undirected graph with weights on edges
- Path: sequence of nodes to reach from one node to another
- cyclic graph: graph that contains a path that makes you reach to same source node
  - Directed Cyclic graph
  - weighted directed cyclic graph
- acyclic graph: no cycle present 
  - acyclic directed graph
  - acyclic weighted directed graph

## Types of Graphs:
1. Undirected Graph
2. Directed Graph

## Graph representations
- Adjacency matrix
  - input: no of edges(m=3), no of nodes (n=3), list of edges ([[0,1],[1,2],[2,0]])
  - adjacency matrix looks like this :[[0,1,0],[0,0,1],[1,0,0]]
  - space complexity:O(n^2)
- Adjacency list
  - input: no of edges(m=3), no of nodes (n=3), list of edges ([[0,1],[1,2],[2,0]])
  - adjacency list is mapping between nodes as keys and values as nodes to which key(node) is connected to or neighbour nodes
  - adjacency list for above looks like: {0:[1,2],1:[0,2],2:[1,0]} (for undirected graph)
