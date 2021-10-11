from graph import Graph
import random

proba = 0.5
def create_graph(n, m):
    """Cree le graph rendom de taille nxm"""
    g = Graph()
    for i in range(n):
        for j in range(m):
            g.addVertice((i,j))
            if i > 0:
                if random.random() < proba:
                    g.addEdge((i,j),(i-1,j))
            if j > 0:
                if random.random() < proba:
                    g.addEdge((i,j),(i,j-1))
    return g

def init_matrix(n, m, value):
    matrix = [[] for i in range(n)]
    for i in range(n):
        matrix[i] = [value for j in range(m)]
    return matrix

def visit(g, v, color, colors, deja_vu):
    i,j = v
    if not(deja_vu[i][j]):
        deja_vu[i][j] = True
        colors[i][j] = color
        for neighbour in g.adjacentTo((i,j)):
            visit(g, neighbour, color, colors, deja_vu)
        return True
    return False
        

def map_color(g, n, m):
    """Associe les couleurs aux composantes connexes du graph"""
    deja_vu = init_matrix(n, m, False)
    colors = init_matrix(n, m, 0)
    color = 1
    for i in range(n):
        for j in range(m):
            if visit(g, (i,j), color, colors, deja_vu):
                color += 1
    return colors
