import sys
import os

class Graph:

    def __init__(self, filename = None, delimiter = None):
        """ Initialise un nouveau graph
        Si un fichier est spécifié en filename, celui-ci est utilisé
        avec le délimiteur entre les noms des sommets"""
        self.graph = {}
        if filename != None:
            with open(filename, "r") as f:
                for line in f:
                    line = line.strip('\n') # Retire \n de la fin de la ligne
                    vertices_list = line.split(delimiter)
                    if vertices_list != []:
                        v = vertices_list[0]
                        for i in range(1,len(vertices_list)):
                            self.addEdge(v, vertices_list[i])

    def vertices(self):
        """Retourne l'ensemble des sommets du graph"""
        return set(list(self.graph))

    def is_vertice(self,v):
        """Retourne True si v est un sommet du graph"""
        return (v in self.graph.keys())

    def addVertice(self, v):
        """ Ajoute un sommet au graph"""
        if not(self.is_vertice(v)):
            self.graph[v] = set()

    def addEdge(self, v, w):
        """ Ajoute une arête de v à w"""
        self.addVertice(v)
        self.addVertice(w)
        self.graph[v].add(w)

    def adjacentTo(self, v):
        """Renvoie l'ensemble des sommets accessibles depuis v
        Remonte l'erreur ValueError si ce sommet n'existe pas"""
        if self.is_vertice(v):
            return self.graph[v]
        else:
            raise ValueError

        
    def listEdges(self):
        edges = []
        for v in self.vertices():
            for w in self.adjacentTo(v):
                edges.append((v,w))
        return edges

    def check_bipartite(self):
        """Vérifie si le graph est bi-partite"""
        vertices = self.vertices()
        partite = {v:-1 for v in vertices}
        tosee = [v for v in vertices]
        if partite != []:
            partite[0] = 0
        while tosee != []:
            v = tosee.pop()
            color = partite[v]
            for w in self.adjacentTo(v):
                if partite[w] == -1: # Le sommet n'a jamais été visité
                    partite[w] = 1 - color # On lui donne la coloration opposée à son voisin
                    tosee.append(w) # On le regardera par la suite
                elif partite[w] == color: # Le graph n'est pas bipartite
                    return False
        return True

    def dot(self, name):
        edges = self.listEdges()
        filename = name + ".dot"
        with open(filename, 'w') as f:
            f.write("digraph " + name + " {")
            for v,w in edges:
                f.write(f"\t{v} -> {w};")
            f.write("}")
        ext = "pdf"
        os.system(f"neato -o{name}.{ext} -T{ext} {name}.dot")











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
        assert edge[1] in g.adjacentTo(edge[0])
        assert not(edge[0] in g.adjacentTo(edge[1]))
    try:
        assert not("world" in g.adjacentTo("tiny"))
    except ValueError:
        assert True

def test_init_from_file():
    g = Graph("tiny.txt")
    edges = [('A','B'),('A','C'),('A','D'),('B','C'),('C','D')]
    for edge in edges:
        assert not(edge[0] in g.adjacentTo(edge[1]))
        assert edge[1] in g.adjacentTo(edge[0])





if __name__ == "__main__" :
    if not(os.path.isfile(sys.argv[1])):
        raise NameError
    
    filename = sys.argv[1]
    g = Graph(filename)
    name = filename.split('.')[0]
    g.dot(name)
    
