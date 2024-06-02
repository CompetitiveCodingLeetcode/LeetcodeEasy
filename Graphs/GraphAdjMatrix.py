class GraphAdjMatrix:
    def __init__(self,n,e,edge_list,is_directed=False):
        self.num_of_nodes = n
        self.num_of_edges = e
        self.edges = edge_list
        self.isDirected = is_directed
        self.adj_matrix = [[0 for j in range(0,self.num_of_nodes)] for i in range(0,self.num_of_nodes)]

    def create_adj_matrix(self):
        for edge in self.edges:
            self.adj_matrix[edge[0]][edge[1]] = 1
            if not self.isDirected:
                self.adj_matrix[edge[1]][edge[0]] = 1

    def print_adj_matrix(self):
        print(self.adj_matrix)

custom_graph = GraphAdjMatrix(3,3,[[0,1],[1,2],[2,0]])
custom_graph.create_adj_matrix()
custom_graph.print_adj_matrix()

directed_custom_graph = GraphAdjMatrix(3,3,[[0,1],[1,2],[2,0]],True)
directed_custom_graph.create_adj_matrix()
directed_custom_graph.print_adj_matrix()