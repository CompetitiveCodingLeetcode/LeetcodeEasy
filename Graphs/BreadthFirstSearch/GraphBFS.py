import queue as q
from Graphs.GraphAdjList import GraphAdjList
class GraphBFS:
    def bfs_traversal(self,g: GraphAdjList):
        ans=[]
        visited = {}
        temp_q = q.Queue(maxsize=g.num_of_nodes)
        for i in range(0,g.num_of_nodes):
            if i not in visited.keys():
                temp_q.put(i)
            while not temp_q.empty():
                temp = temp_q.get()
                if temp not in visited.keys():
                    visited[temp] = True
                    ans.append(temp)
                vals = g.adj_list[temp]
                j=0
                while j<len(vals):
                    if vals[j] not in visited.keys():
                        temp_q.put(vals[j])
                    j += 1
        return ans

    def get_bfs_traversal(self,g):
        print(self.bfs_traversal(g))

c_graph = GraphAdjList(6,5,[[0,3],[3,1],[1,2],[1,4],[5,6]])
c_graph.create_adj_list()
c_graph.print_adj_list()

g = GraphBFS()
g.get_bfs_traversal(c_graph)