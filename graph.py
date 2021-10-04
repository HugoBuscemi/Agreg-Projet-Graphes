class Graph:

    def __init__(self):
        self.graph = {}

    def vertices(self):
        return set(list(self.graph))

    def addVertice(self, v):
        if not( v in self.vertices()):
            self.graph[v] = set()

    def addEdge(self, v, w):
        self.addVertice(v)
        self.addVertice(w)
        self.graph[v].add(w)
        self.graph[w].add(v)

    def adjacentTo(self, v):
        if (v in self.vertices()):
            return self.graph[v]
        else:
            raise ValueError















# ==== Tests =====

def test_graph_init():
    g = Graph()


def test_graph_addVertice():
    g = Graph()
    keys = ["Hello", "small", "world"]
    for key in keys:
        g.addVertice(key)
    vertices = g.vertices()
    for key in keys:
        assert key in vertices

def test_addEdge():
    g = Graph()
    edges = [("Hello", "world"), ("small", "world")]
    for edge in edges:
        g.addEdge(edge[0], edge[1])
    for edge in edges:
        assert edge[0] in g.adjacentTo(edge[1])
        assert edge[1] in g.adjacentTo(edge[0])
    try:
        assert not("world" in g.adjacentTo("tiny"))
    except ValueError:
        assert True
