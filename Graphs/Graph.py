class Graph:
    def __init__(self,gdict = None):
        if gdict is None:
            self.gdict = {}
        self.gdict = gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)


custom_dict = {
    "a":["b","c"],
    "b":["c","d","e"],
    "c":["e","f"]
}

custom_graph = Graph(custom_dict)
print(custom_graph.gdict)
custom_graph.addEdge("c","g")
print(custom_graph.gdict)