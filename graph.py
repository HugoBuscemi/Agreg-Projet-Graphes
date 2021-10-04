class Graph:

    def __init__(self):
        self.graph = {}

    def addVertice(self, v):
        self.graph[v] = set()

    def addEdge(self, v, w):
        self.graph[v].add(w)
        self.graph[w].add(v)

    def vertices(self):
        return set(list(self.graph))

    def adjacentTo(self, v):
        return self.graph[v]

