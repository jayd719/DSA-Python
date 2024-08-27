class Graph(object):
    def __init__(self,graph_dic = {}):
        self.graph_dic = graph_dic

    
    def edges(self, node):
        return self.graph_dic[node]
    def get_all_nodes(self):
        return self.graph_dic.keys()
    
    def add_node(self,node):
        if(node not in self.graph_dic):
            self.graph_dic[node]={}
            
    def add_edge(self,start,end):
        # check if start node is already in the graph- only add it start node is present in graph
        if(start in self.graph_dic):
            self.graph_dic[start].add(end)
            if(end not in self.graph_dic):
                self.graph_dic[end]={}
            self.graph_dic[end].add(start)
        


#Graph 
g = { "a" : {"d"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c"},
      "e" : {"c"},
      "f" : {}
    }


# create new graph instance
graph = Graph(g)
graph.add_node("g")
print(graph.graph_dic)
print(graph.edges("b"))
print(graph.get_all_nodes())




