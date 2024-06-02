class GraphAdjList:
    def __init__(self,n,e,edge_list,is_directed=False):
        self.num_of_nodes = n
        self.num_of_edges = e
        self.edges = edge_list
        self.isDirected = is_directed
        self.adj_list = {}

    def create_adj_list(self):
        for edge in self.edges:
            if edge[0] in self.adj_list.keys():
                self.adj_list[edge[0]].append(edge[1])
                if not self.isDirected:
                    if edge[1] in self.adj_list.keys():
                        self.adj_list[edge[1]].append(edge[0])
                    else:
                        self.adj_list[edge[1]] = [edge[0]]
            else:
                self.adj_list[edge[0]] = [edge[1]]
                if not self.isDirected:
                    if edge[1] in self.adj_list.keys():
                        self.adj_list[edge[1]].append(edge[0])
                    else:
                        self.adj_list[edge[1]] = [edge[0]]

    def print_adj_list(self):
        print(self.adj_list)

custom_graph = GraphAdjList(3,3,[[0,1],[1,2],[2,0]])
custom_graph.create_adj_list()
custom_graph.print_adj_list()

directed_custom_graph = GraphAdjList(3,3,[[0,1],[1,2],[2,0]],True)
directed_custom_graph.create_adj_list()
directed_custom_graph.print_adj_list()