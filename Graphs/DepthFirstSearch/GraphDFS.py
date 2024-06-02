from Graphs.GraphAdjList import GraphAdjList
class GraphDFS:
    def dfs_traversal(self,g: GraphAdjList,visited,component_ans,i):
        if i not in visited.keys():
            visited[i] = True
            component_ans.append(i)
        else:
            return
        for j in g.adj_list[i]:
            self.dfs_traversal(g,visited,component_ans,j)

    def get_dfs_traversal(self,g):
        visited = {}
        ans = []
        for i in range(0, g.num_of_nodes):
            if i not in visited.keys():
                component_ans = []
                self.dfs_traversal(g,visited,component_ans,i)
                ans.append(component_ans)
        return ans
c_graph = GraphAdjList(9,9,[[0,4],[4,2],[2,3],[3,5],[5,1],[1,4],[6,7],[7,8],[8,6]])
c_graph.create_adj_list()
c_graph.print_adj_list()

g = GraphDFS()
print(g.get_dfs_traversal(c_graph))